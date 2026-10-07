"""Fetch Carrefour UAE / KSA / Egypt prices through an Apify Actor.

Usage: APIFY_TOKEN=... python carrefour.py AE milk rice --max 100
"""
import argparse
import os

from apify_client import ApifyClient

ACTOR = "alfhar/carrefour-price-tracker-mena"


def get_prices(country, keywords, max_products=100, only_discounted=False, token=None):
    client = ApifyClient(token or os.environ["APIFY_TOKEN"])
    run = client.actor(ACTOR).call(
        run_input={
            "country": country,  # AE, SA or EG
            "categoryKeywords": keywords,
            "maxProducts": max_products,
            "onlyDiscounted": only_discounted,
        }
    )
    return list(client.dataset(run["defaultDatasetId"]).iterate_items())


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("country", choices=["AE", "SA", "EG"])
    ap.add_argument("keywords", nargs="+")
    ap.add_argument("--max", type=int, default=100)
    ap.add_argument("--discounted", action="store_true")
    a = ap.parse_args()
    for p in get_prices(a.country, a.keywords, a.max, a.discounted):
        print(p["name"], p["price"], p["currency"], p.get("discountPercent"))
