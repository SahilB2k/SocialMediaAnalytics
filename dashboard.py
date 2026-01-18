import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from textblob import TextBlob
from wordcloud import WordCloud

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Social Media Business Dashboard",
    layout="wide"
)

# -----------------------------------
# LOAD DATA
# -----------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_data.csv")

df = load_data()

# -----------------------------------
# SIDEBAR FILTERS (DYNAMIC)
# -----------------------------------
st.sidebar.title("🔍 Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    ["Positive", "Neutral", "Negative"],
    default=["Positive", "Neutral", "Negative"]
)

author_filter = st.sidebar.multiselect(
    "Select Author",
    df["author"].unique()
)

# SENTIMENT COMPUTATION
df["sentiment"] = df["cleaned_text"].apply(
    lambda x: "Positive" if TextBlob(x).sentiment.polarity > 0
    else "Negative" if TextBlob(x).sentiment.polarity < 0
    else "Neutral"
)

# APPLY FILTERS
filtered_df = df[df["sentiment"].isin(sentiment_filter)]

if author_filter:
    filtered_df = filtered_df[filtered_df["author"].isin(author_filter)]

# -----------------------------------
# HEADER
# -----------------------------------
st.title("📊 Social Media Analytics Dashboard")
st.caption("Interactive Business Intelligence from Social Media Data")

# -----------------------------------
# KPI METRICS (COMPACT)
# -----------------------------------
k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Posts", len(filtered_df))
k2.metric("Authors", filtered_df["author"].nunique())
k3.metric("Topics", filtered_df["tags"].str.split(", ").explode().nunique())
k4.metric("Avg Length", int(filtered_df["cleaned_text"].apply(len).mean()))

st.divider()

# -----------------------------------
# ROW 1: SENTIMENT + WORD CLOUD
# -----------------------------------
c1, c2 = st.columns(2)

with c1:
    st.subheader("😊 Sentiment Distribution")
    fig, ax = plt.subplots(figsize=(4, 3))
    filtered_df["sentiment"].value_counts().plot(kind="bar", ax=ax)
    ax.set_ylabel("Count")
    st.pyplot(fig)

with c2:
    st.subheader("☁️ Content Word Cloud")

    text = " ".join(filtered_df["cleaned_text"])
    wc = WordCloud(
        width=400,
        height=250,
        background_color="white"
    ).generate(text)

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

st.divider()

# -----------------------------------
# ROW 2: TOPICS + TREND
# -----------------------------------
c3, c4 = st.columns(2)

with c3:
    st.subheader("📌 Top Topics")
    tags = filtered_df["tags"].str.split(", ").explode()
    fig, ax = plt.subplots(figsize=(4, 3))
    tags.value_counts().head(8).plot(kind="bar", ax=ax)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

with c4:
    st.subheader("📉 Content Trend")
    fig, ax = plt.subplots(figsize=(4, 3))
    filtered_df.groupby("page").size().plot(marker="o", ax=ax)
    ax.set_xlabel("Page Index")
    ax.set_ylabel("Posts")
    st.pyplot(fig)

st.divider()

# -----------------------------------
# ROW 3: INFLUENCE TABLE
# -----------------------------------
st.subheader("⭐ Influential Users")

influence = filtered_df["author"].value_counts().head(10)
st.dataframe(influence.rename("Post Count"))

st.divider()

# -----------------------------------
# OPTIONAL: NETWORK SNAPSHOT (SMALL)
# -----------------------------------
st.subheader("🧩 Community Structure (Snapshot)")

G = nx.Graph()
for _, row in filtered_df.head(30).iterrows():  # limit for clarity
    for tag in row["tags"].split(", "):
        G.add_edge(row["author"], tag)

fig, ax = plt.subplots(figsize=(5, 4))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, node_size=40, with_labels=False, ax=ax)
st.pyplot(fig)

# -----------------------------------
# REPORT DOWNLOAD
# -----------------------------------
st.subheader("📄 Business Report")

st.download_button(
    "Download CSV Report",
    filtered_df.to_csv(index=False),
    "filtered_social_media_report.csv",
    "text/csv"
)

st.success("Dashboard loaded successfully ✔")
