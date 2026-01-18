import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import logging
from logger import setup_logger

setup_logger()

def structure_based_analysis():
    logging.info("Loading cleaned data")
    df = pd.read_csv("data/cleaned_data.csv")

    # -----------------------------------------
    # 1️⃣ NETWORK CONSTRUCTION
    # -----------------------------------------
    logging.info("Building user interaction network")

    G = nx.Graph()

    for _, row in df.iterrows():
        author = row["author"]
        tags = row["tags"].split(", ")

        for tag in tags:
            G.add_node(author)
            G.add_node(tag)
            G.add_edge(author, tag)

    logging.info(f"Total Nodes: {G.number_of_nodes()}")
    logging.info(f"Total Edges: {G.number_of_edges()}")

    print("Nodes:", G.number_of_nodes())
    print("Edges:", G.number_of_edges())

    # -----------------------------------------
    # 2️⃣ COMMUNITY DETECTION
    # -----------------------------------------
    logging.info("Performing community detection")

    communities = nx.algorithms.community.greedy_modularity_communities(G)
    community_map = {}

    for i, community in enumerate(communities):
        for node in community:
            community_map[node] = i

    nx.set_node_attributes(G, community_map, "community")

    print("\nDetected Communities:", len(communities))

    # -----------------------------------------
    # 3️⃣ INFLUENCE ANALYSIS
    # -----------------------------------------
    logging.info("Calculating influence scores")

    degree_centrality = nx.degree_centrality(G)

    top_influencers = sorted(
        degree_centrality.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    influencer_df = pd.DataFrame(
        top_influencers,
        columns=["Node", "Influence Score"]
    )

    print("\nTop Influential Nodes:")
    print(influencer_df)

    # -----------------------------------------
    # 4️⃣ NETWORK VISUALIZATION
    # -----------------------------------------
    logging.info("Visualizing social network structure")

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)

    node_colors = [community_map.get(node, 0) for node in G.nodes()]

    nx.draw(
        G,
        pos,
        node_color=node_colors,
        cmap=plt.cm.tab10,
        node_size=50,
        with_labels=False
    )

    plt.title("Structure-Based Social Media Network")
    plt.show()

    logging.info("Structure-based analysis completed")


if __name__ == "__main__":
    structure_based_analysis()
