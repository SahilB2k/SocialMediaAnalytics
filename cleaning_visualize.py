import pandas as pd
import matplotlib.pyplot as plt
import logging
from logger import setup_logger

setup_logger()

def visualize_cleaning_effect():
    logging.info("Loading datasets")
    
    raw = pd.read_csv("data/raw_data.csv")
    clean = pd.read_csv("data/cleaned_data.csv")

    # -------------------------------
    # 1️⃣ CHARACTER COUNT COMPARISON
    # -------------------------------
    logging.info("Calculating character counts")

    total_raw_chars = raw["quote"].apply(len).sum()
    total_clean_chars = clean["cleaned_text"].apply(len).sum()

    print("Total characters BEFORE cleaning:", total_raw_chars)
    print("Total characters AFTER cleaning:", total_clean_chars)

    plt.figure()
    plt.bar(
        ["Before Cleaning", "After Cleaning"],
        [total_raw_chars, total_clean_chars]
    )
    plt.title("Total Number of Characters Before vs After Cleaning")
    plt.ylabel("Character Count")
    plt.show()

    # -------------------------------
    # 2️⃣ AVERAGE TEXT LENGTH
    # -------------------------------
    avg_raw = raw["quote"].apply(len).mean()
    avg_clean = clean["cleaned_text"].apply(len).mean()

    plt.figure()
    plt.bar(
        ["Raw Text", "Cleaned Text"],
        [avg_raw, avg_clean]
    )
    plt.title("Average Text Length Comparison")
    plt.ylabel("Average Characters")
    plt.show()

    # -------------------------------
    # 3️⃣ TOP WORDS AFTER CLEANING
    # -------------------------------
    logging.info("Extracting top words")

    words = clean["cleaned_text"].str.split().explode()
    top_words = words.value_counts().head(10)

    plt.figure()
    top_words.plot(kind="bar")
    plt.title("Top 10 Frequent Words After Cleaning")
    plt.ylabel("Frequency")
    plt.show()

    # -------------------------------
    # 4️⃣ MISSING VALUE CHECK (FIXED)
    # -------------------------------
    missing_counts = clean.isnull().sum()

    print("\nMissing Values After Cleaning:")
    print(missing_counts)

    if missing_counts.sum() == 0:
        print("\n✅ No missing values found after cleaning.")
    else:
        plt.figure()
        missing_counts.plot(kind="bar")
        plt.title("Missing Values After Cleaning")
        plt.ylabel("Count")
        plt.show()

    logging.info("Visualization completed successfully")


if __name__ == "__main__":
    visualize_cleaning_effect()
