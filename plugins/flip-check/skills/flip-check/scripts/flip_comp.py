#!/usr/bin/env python3
"""
flip_comp.py — pull real eBay comps + a velocity proxy for a flip-check.

Uses the SerpApi eBay engine. Fetches SOLD listings (real comps, not asking
prices) and ACTIVE listings (to estimate sell-through), filters both to true
matches, and prints median/range/count plus a rough velocity read.

Key handling (never hardcoded):
  - reads the SERPAPI_KEY environment variable, or
  - reads a key file path from SERPAPI_KEY_FILE, or
  - reads ~/.config/flip-check/serpapi.key if it exists.

Usage:
  SERPAPI_KEY=xxx python3 flip_comp.py "Jigsaw merino sweater" \
      --must-have jigsaw merino --domain ebay.com
"""
import sys, os, json, argparse, statistics, urllib.parse, urllib.request


def load_key():
    k = os.environ.get("SERPAPI_KEY")
    if k:
        return k.strip()
    path = os.environ.get("SERPAPI_KEY_FILE") or os.path.expanduser(
        "~/.config/flip-check/serpapi.key"
    )
    if path and os.path.exists(path):
        return open(path).read().strip()
    sys.exit(
        "No SerpApi key. Set SERPAPI_KEY env var, or SERPAPI_KEY_FILE, or "
        "create ~/.config/flip-check/serpapi.key"
    )


FATAL_HINTS = ("api key", "run out", "invalid", "unauthorized", "credit")


def _call(url):
    with urllib.request.urlopen(url, timeout=45) as r:
        return json.load(r)


def query(nkw, key, sold=False, domain="ebay.com", retries=2):
    params = {
        "engine": "ebay",
        "_nkw": nkw,
        "ebay_domain": domain,
        "api_key": key,
    }
    if sold:
        params["show_only"] = "Sold"
    else:
        # _ipg=100 widens active results, but it BREAKS the sold scrape
        # (returns "no results"), so only set it for active queries.
        params["_ipg"] = "100"
    url = "https://serpapi.com/search?" + urllib.parse.urlencode(params)

    last_err = None
    for attempt in range(retries + 1):
        try:
            data = _call(url)
        except Exception as e:  # network blip
            last_err = str(e)
            continue
        err = data.get("error")
        if not err:
            return data.get("organic_results", [])
        # Auth/credit problems are fatal; "no results" is transient — retry/tolerate.
        if any(h in err.lower() for h in FATAL_HINTS):
            sys.exit("SerpApi error (fatal): " + str(err))
        last_err = err  # e.g. "eBay hasn't returned any results for this query."
    # Exhausted retries on a non-fatal error: treat as empty, warn on stderr.
    sys.stderr.write(
        f"[warn] {'sold' if sold else 'active'} query returned nothing "
        f"after {retries + 1} tries: {last_err}\n"
    )
    return []


def relevant(items, must_have, exclude):
    out = []
    for it in items:
        t = (it.get("title") or "").lower()
        if must_have and not all(w.lower() in t for w in must_have):
            continue
        if exclude and any(w.lower() in t for w in exclude):
            continue
        out.append(it)
    return out


def price_list(items):
    return sorted(
        it["price"]["extracted"]
        for it in items
        if isinstance(it.get("price"), dict) and it["price"].get("extracted")
    )


def pctl(ps, q):
    if not ps:
        return None
    i = min(len(ps) - 1, int(q * len(ps)))
    return ps[i]


def stats(ps):
    if not ps:
        return None
    return {
        "count": len(ps),
        "median": round(statistics.median(ps), 2),
        "min": ps[0],
        "max": ps[-1],
        "p25": round(pctl(ps, 0.25), 2),
        "p75": round(pctl(ps, 0.75), 2),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", help="eBay search terms, e.g. 'Jigsaw merino sweater'")
    ap.add_argument("--must-have", nargs="*", default=[],
                    help="words that MUST appear in a listing title to count")
    ap.add_argument("--exclude", nargs="*", default=[],
                    help="words that disqualify a listing (e.g. mens kids)")
    ap.add_argument("--domain", default="ebay.com")
    ap.add_argument("--json", action="store_true", help="emit JSON only")
    args = ap.parse_args()

    key = load_key()
    sold_raw = query(args.query, key, sold=True, domain=args.domain)
    active_raw = query(args.query, key, sold=False, domain=args.domain)

    sold = relevant(sold_raw, args.must_have, args.exclude)
    active = relevant(active_raw, args.must_have, args.exclude)

    sold_ps = price_list(sold)
    sold_stats = stats(sold_ps)
    active_stats = stats(price_list(active))

    sold_n, active_n = len(sold), len(active)
    str_pct = round(100 * sold_n / (sold_n + active_n)) if (sold_n + active_n) else None

    result = {
        "query": args.query,
        "must_have": args.must_have,
        "sold": sold_stats,
        "active_asking": active_stats,
        "velocity": {
            "sold_matches": sold_n,
            "active_matches": active_n,
            "sell_through_pct": str_pct,
            "note": "proxy: sold / (sold + active) on first result page (~100 each)",
        },
        "sold_examples": [
            {"price": it["price"]["raw"], "cond": it.get("condition"),
             "title": it.get("title")}
            for it in sold[:6]
        ],
    }

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print(f"\n=== FLIP COMP: {args.query!r}  (filter: {args.must_have}) ===")
    if sold_stats:
        s = sold_stats
        print(f"SOLD (real comps): n={s['count']}  median ${s['median']}  "
              f"range ${s['min']}-${s['max']}  mid ${s['p25']}-${s['p75']}")
    else:
        print("SOLD: no matched sold comps found — treat as a guess, be conservative.")
    if active_stats:
        a = active_stats
        print(f"ACTIVE asking:     n={a['count']}  median ${a['median']}  "
              f"range ${a['min']}-${a['max']}")
    if str_pct is not None:
        v = "hot" if str_pct >= 50 else ("ok" if str_pct >= 40 else "SLOW")
        print(f"VELOCITY proxy:    sell-through ~{str_pct}%  ({v})  "
              f"[{sold_n} sold vs {active_n} active]")
    print("\nSold examples:")
    for ex in result["sold_examples"]:
        print(f"  {ex['price']:>9}  {ex['cond'] or '':<12}  {ex['title'][:64]}")
    print()


if __name__ == "__main__":
    main()
