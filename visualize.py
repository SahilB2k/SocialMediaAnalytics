import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from logger import setup_logger

setup_logger()

def visualize():
    logging.info("Loading scraped data")
    df = pd.read_csv("data/scraped_data.csv")

    # Quote length analysis (content depth)
    df["quote_length"] = df["quote"].apply(len)

    plt.figure()
    sns.histplot(df["quote_length"], bins=10)
    plt.title("Quote Length Distribution (Content Depth)")
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.show()

    # Author popularity
    plt.figure()
    df["author"].value_counts().head(10).plot(kind="bar")
    plt.title("Top Authors (Content Contributors)")
    plt.ylabel("Number of Quotes")
    plt.show()

    # Tag usage (topics)
    all_tags = df["tags"].str.split(", ").explode()

    plt.figure()
    all_tags.value_counts().head(10).plot(kind="bar")
    plt.title("Most Common Topics (Tags)")
    plt.ylabel("Frequency")
    plt.show()

    logging.info("Visualization completed")


if __name__ == "__main__":
    visualize()
