import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob
import logging
from logger import setup_logger

setup_logger()

def content_based_analytics():
    logging.info("Loading cleaned data")
    df = pd.read_csv("data/cleaned_data.csv")

    # ----------------------------------
    # 1️⃣ SENTIMENT / OPINION ANALYSIS
    # ----------------------------------
    logging.info("Performing sentiment analysis")

    df["sentiment_score"] = df["cleaned_text"].apply(
        lambda x: TextBlob(x).sentiment.polarity
    )

    df["sentiment_label"] = df["sentiment_score"].apply(
        lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Neutral"
    )

    print("\nSentiment Distribution:")
    print(df["sentiment_label"].value_counts())

    plt.figure()
    df["sentiment_label"].value_counts().plot(kind="bar")
    plt.title("Sentiment Distribution of Social Media Content")
    plt.ylabel("Count")
    plt.show()

    # ----------------------------------
    # 2️⃣ TOPIC / ISSUE ANALYSIS
    # ----------------------------------
    logging.info("Performing topic analysis")

    vectorizer = CountVectorizer(max_features=10)
    X = vectorizer.fit_transform(df["cleaned_text"])

    topics = vectorizer.get_feature_names_out()
    topic_counts = X.sum(axis=0).A1

    topic_df = pd.DataFrame({
        "Topic": topics,
        "Frequency": topic_counts
    }).sort_values(by="Frequency", ascending=False)

    print("\nTop Topics:")
    print(topic_df)

    plt.figure()
    plt.bar(topic_df["Topic"], topic_df["Frequency"])
    plt.title("Top Topics in Social Media Content")
    plt.ylabel("Frequency")
    plt.show()

    # ----------------------------------
    # 3️⃣ TREND ANALYSIS (CONTENT VOLUME)
    # ----------------------------------
    logging.info("Performing trend analysis")

    plt.figure()
    df.groupby("page").size().plot(marker="o")
    plt.title("Trend Analysis: Content Volume Across Pages")
    plt.xlabel("Page Number")
    plt.ylabel("Number of Posts")
    plt.show()

    logging.info("Content-based analytics completed")


if __name__ == "__main__":
    content_based_analytics()
