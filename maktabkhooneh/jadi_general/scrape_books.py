"""
Web Scraping Project
---------------------
Extracts from a target web page:
  1. The page title
  2. Text content from a specific HTML class (e.g. book/product titles)
  3. Image links found on the page

Target site: https://webscraper.io/test-sites/e-commerce/static/computers/laptops

This is a public "sandbox" site built specifically for practicing
web scraping, so it's safe and reliable to use for this exercise.

Libraries used: requests, BeautifulSoup (bs4)
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ----------------------------
# 1. INPUTS
# ----------------------------
URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"   # website to scrape
TARGET_CLASS = "title"          # HTML class that wraps each book item


def fetch_page(url):
    """Connect to the website and return the raw HTML response."""
    headers = {"User-Agent": "Mozilla/5.0 (educational scraping project)"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # raise an error for bad status codes (4xx/5xx)
    return response.text


def parse_page_title(soup):
    """Extract the main <title> of the web page."""
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return "No title found"


def parse_item_titles(soup, class_name):
    """
    Extract titles from elements belonging to a specific class.
    On books.toscrape.com each book is wrapped in <article class="product_pod">,
    and the title lives in the <h3><a title="..."> tag.
    """
    titles = []
    items = soup.find_all(class_=class_name)
    for item in items:
        link_tag = item.find("h3").find("a") if item.find("h3") else None
        if link_tag and link_tag.get("title"):
            titles.append(link_tag["title"].strip())
    return titles


def parse_image_links(soup, base_url):
    """Extract all image links on the page, converted to absolute URLs."""
    image_links = []
    for img_tag in soup.find_all("img"):
        src = img_tag.get("src")
        if src:
            image_links.append(urljoin(base_url, src))
    return image_links


def main():
    print(f"Connecting to: {URL}\n")
    html = fetch_page(URL)
    soup = BeautifulSoup(html, "html.parser")

    # --- Extract data ---
    page_title = parse_page_title(soup)
    item_titles = parse_item_titles(soup, TARGET_CLASS)
    image_links = parse_image_links(soup, URL)

    # --- Output results ---
    print("PAGE TITLE")
    print("-" * 40)
    print(page_title)

    print(f"\nBOOK TITLES (class='{TARGET_CLASS}') — {len(item_titles)} found")
    print("-" * 40)
    for i, title in enumerate(item_titles, start=1):
        print(f"{i}. {title}")

    print(f"\nIMAGE LINKS — {len(image_links)} found")
    print("-" * 40)
    for i, link in enumerate(image_links, start=1):
        print(f"{i}. {link}")


if __name__ == "__main__":
    main()
