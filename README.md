
[scrapping.py](https://github.com/user-attachments/files/23635273/scrapping.py)
"""quotes-scraper: simple web scraper for quotes.toscrape.com

Usage:
    python scrapping.py            # run with defaults
    python scrapping.py --keywords life love
"""
from typing import List
import requests
from bs4 import BeautifulSoup
import argparse
import sys

def fetch_quotes(url: str) -> List[dict]:
    """Fetch quotes from a single page of quotes.toscrape.com."""
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'lxml')
    quote_blocks = soup.find_all('div', class_='quote')
    results = []
    for q in quote_blocks:
        text_tag = q.find('span', class_='text')
        author_tag = q.find('small', class_='author')
        if text_tag and author_tag:
            results.append({
                'text': text_tag.get_text(strip=True),
                'author': author_tag.get_text(strip=True),
            })
    return results

def filter_quotes(quotes: List[dict], keywords: List[str]) -> List[dict]:
    """Return quotes that contain any of the keywords (case-insensitive)."""
    if not keywords:
        return quotes
    lower_keys = [k.lower() for k in keywords]
    out = []
    for q in quotes:
        txt = q['text'].lower()
        if any(k in txt for k in lower_keys):
            out.append(q)
    return out

def main(argv=None):
    parser = argparse.ArgumentParser(description='Simple quotes scraper for quotes.toscrape.com')
    parser.add_argument('--url', default='https://quotes.toscrape.com/', help='URL to scrape')
    parser.add_argument('--keywords', nargs='*', default=['life','love','inspirational','humor','books','reading','friendship','friends','truth','simile'],
                        help='Keywords to filter quotes (space separated)')
    parser.add_argument('--limit', type=int, default=0, help='Limit number of printed quotes (0 means no limit)')
    args = parser.parse_args(argv)

    try:
        quotes = fetch_quotes(args.url)
    except Exception as e:
        print(f'Error fetching quotes: {e}', file=sys.stderr)
        sys.exit(1)

    filtered = filter_quotes(quotes, args.keywords)
    if not filtered:
        print('No quotes found matching keywords.')
        return

    count = 0
    for q in filtered:
        print(f"{q['text']}  - {q['author']}")
        count += 1
        if args.limit and count >= args.limit:
            break

if __name__ == '__main__':
    main()
