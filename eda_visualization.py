import pandas as pd
import matplotlib.pyplot as plt
import logging
from logger import setup_logger

setup_logger()

def perform_eda():
    logging.info("Loading cleaned data for EDA")
    df = pd.read_csv("data/cleaned_data.csv")

    print("\nDataset Info:")
    print(df.info())

    print("\nStatistical Summary:")
    print(df.describe(include="all"))

    # -----------------------------------
    # 1️⃣ CONTENT LENGTH ANALYSIS
    # -----------------------------------
    df["text_length"] = df["cleaned_text"].apply(len)

    plt.figure()
    plt.hist(df["text_length"], bins=10)
    plt.title("Distribution of Cleaned Text Length")
    plt.xlabel("Number of Characters")
    plt.ylabel("Frequency")
    plt.show()

    # Business Insight:
    # Helps understand content depth and consistency

    # -----------------------------------
    # 2️⃣ TOP AUTHORS (CONTENT CONTRIBUTORS)
    # -----------------------------------
    plt.figure()
    df["author"].value_counts().head(10).plot(kind="bar")
    plt.title("Top Content Contributors (Authors)")
    plt.ylabel("Number of Quotes")
    plt.show()

    # Business Insight:
    # Identifies influential contributors

    # -----------------------------------
    # 3️⃣ TOP BUSINESS TOPICS (TAGS)
    # -----------------------------------
    tags = df["tags"].str.split(", ").explode()

    plt.figure()
    tags.value_counts().head(10).plot(kind="bar")
    plt.title("Most Frequent Topics (Tags)")
    plt.ylabel("Frequency")
    plt.show()

    # Business Insight:
    # Shows what topics dominate user discussions

    # -----------------------------------
    # 4️⃣ CONTENT CONSISTENCY CHECK
    # -----------------------------------
    plt.figure()
    plt.boxplot(df["text_length"])
    plt.title("Text Length Variability (Outlier Detection)")
    plt.ylabel("Characters")
    plt.show()

    # Business Insight:
    # Detects unusually long or short content

    logging.info("EDA and visualization completed successfully")


if __name__ == "__main__":
    perform_eda()
