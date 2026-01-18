import pandas as pd
import numpy as np
import re
import logging
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from pymongo import MongoClient
from logger import setup_logger

setup_logger()

nltk.download("stopwords")

STOP_WORDS = set(stopwords.words("english"))
STEMMER = PorterStemmer()

# -------------------------------
# TEXT CLEANING FUNCTIONS
# -------------------------------

def normalize_text(text):
    logging.info("Normalizing text")
    text = text.strip()                 # remove whitespaces
    text = text.lower()                 # lowercase
    text = text.encode("utf-8", "ignore").decode()
    return text


def remove_urls(text):
    return re.sub(r"http\S+|www\S+", "", text)


def remove_special_chars(text):
    return re.sub(r"[^a-zA-Z\s]", "", text)


def tokenize(text):
    return text.split()


def remove_stopwords(tokens):
    return [word for word in tokens if word not in STOP_WORDS]


def stemming(tokens):
    return [STEMMER.stem(word) for word in tokens]


def slang_lookup(tokens):
    slang_dict = {
        "luv": "love",
        "u": "you",
        "ur": "your"
    }
    return [slang_dict.get(word, word) for word in tokens]


# -------------------------------
# CLEANING PIPELINE
# -------------------------------

def clean_text_pipeline(text):
    text = normalize_text(text)
    text = remove_urls(text)
    text = remove_special_chars(text)

    tokens = tokenize(text)
    tokens = slang_lookup(tokens)
    tokens = remove_stopwords(tokens)
    tokens = stemming(tokens)

    return " ".join(tokens)


# -------------------------------
# STORAGE FUNCTIONS
# -------------------------------

def store_to_csv(df):
    df.to_csv("data/cleaned_data.csv", index=False)
    logging.info("Cleaned data stored in CSV")


def store_to_mongodb(df):
    logging.info("Storing data into MongoDB")

    client = MongoClient("mongodb://localhost:27017/")
    db = client["business_analytics"]
    collection = db["cleaned_social_data"]

    collection.insert_many(df.to_dict("records"))
    logging.info("Data successfully stored in MongoDB")


# -------------------------------
# MAIN FUNCTION
# -------------------------------

def clean_and_store():
    logging.info("Loading raw data")
    df = pd.read_csv("data/raw_data.csv")

    logging.info("Starting data cleaning process")
    df["cleaned_text"] = df["quote"].apply(clean_text_pipeline)

    df = df.dropna()
    df = df.drop_duplicates()

    logging.info("Cleaning completed")
    print("\nCleaned Data Sample:\n", df[["cleaned_text"]].head())

    store_to_csv(df)
    # Optional MongoDB storage
    # store_to_mongodb(df)


if __name__ == "__main__":
    clean_and_store()
