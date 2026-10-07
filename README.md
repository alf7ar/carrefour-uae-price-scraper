# carrefour-uae-price-scraper

A tiny Python client to get Carrefour grocery prices for the **UAE (AED), Saudi Arabia (SAR) and Egypt (EGP)** as JSON: price, original price, discount percent, unit price per kg or litre, stock status.

## The problem

Carrefour has no public price API for the MENA sites (carrefouruae.com, carrefourksa.com, carrefouregypt.com). Most price-comparison tools cover Europe; if you need local-currency MENA prices for tracking, deal feeds or research, you have to extract them yourself. This repo calls a hosted [Apify Actor](https://apify.com/alfhar/carrefour-price-tracker-mena) that does it with plain HTTP requests on public pages and respects Carrefour's robots.txt.

> **Disclosure:** the Apify Actor linked here was built by the author of this repo. It is a paid Actor (pay per event, about $0.002 per product plus a small start fee; check the Actor page for current prices). You need an Apify account and API token. This client is MIT licensed.

## Quick start

```bash
pip install -r requirements.txt
export APIFY_TOKEN=your_token_here
python carrefour.py AE milk rice --max 100
python carrefour.py SA water juice --discounted
```

From your own code:

```python
from carrefour import get_prices

for p in get_prices("AE", ["milk"], max_products=50):
    print(p["name"], p["price"], p["currency"])
```

## Example output

Shortened sample (Carrefour Saudi Arabia), see [`example_output.json`](example_output.json):

| name | price | original | currency | discount % | unit price |
|---|---|---|---|---|---|
| Aquafina Drinking Water Bottle 1.5L x 6 | 5.99 | 8.5 | SAR | 29.5 | 0.67 SAR/l |

## Notes

- Prices are the public online prices for Carrefour's default delivery area and can differ by store.
- The Actor reads the first page of each category and walks subcategories; it does not use Carrefour search or page-number URLs (disallowed by robots.txt).
- Not affiliated with Carrefour.

## Links

- Apify Actor: https://apify.com/alfhar/carrefour-price-tracker-mena (built by the author of this repo)

## License

MIT
