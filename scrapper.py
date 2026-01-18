import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
from logger import setup_logger

setup_logger()

BASE_URL = "https://quotes.toscrape.com/page/{}/"

def scrape_website(pages=5):
    logging.info("Starting data collection from single free website")

    all_data = []

    for page in range(1, pages + 1):
        url = BASE_URL.format(page)
        logging.info(f"Crawling page {page}: {url}")

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        logging.info(f"Found {len(quotes)} records on page {page}")

        for i, quote in enumerate(quotes):
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]

            record = {
                "quote": text,
                "author": author,
                "tags": ", ".join(tags),
                "page": page
            }

            all_data.append(record)
            logging.info(f"Parsed record {i+1} from page {page}")

    df = pd.DataFrame(all_data)
    df.to_csv("data/scraped_data.csv", index=False)

    logging.info("Data scraping completed")
    print("\nSample Data:\n", df.head())

    return df


if __name__ == "__main__":
    scrape_website(pages=5)
