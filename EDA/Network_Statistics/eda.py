import networkx as nx
import pandas as pd

from Network import init_network
from functools import lru_cache
from pretty_html_table import build_table
from decimal import *


@lru_cache()
def eda_caller(G):
    funcs = [get_number_of_nodes, get_number_of_edges, get_average_degree,
             get_average_clustering, get_average_shortest_path,
             get_diameter, get_degree_centrality, get_betweenness_centrality,
             get_closeness_centrality, get_max_degree, get_min_degree]

    func_description = ["# Nodes", "# Edges", "Average Degree",
                        "Average Clustering", "Average Shortest Path",
                        "Diameter", "Degree Centrality", "Betweenness Centrality",
                        "Closeness Centrality", "Max Degree", "Min Degree"]

    eda = {}

    func_dict = zip(funcs, func_description)

    for func, description in func_dict:
        eda[description] = func(G)

    return eda


def extract_single_valued_statistics_to_dataframe(eda):
    eda = {k: v for k, v in eda.items() if type(v) in [float, int]}
    eda = pd.DataFrame(eda.items())

    def __format(x):
        """very disgusting must be fixed"""
        x = round(x, 2)
        x = str(x)
        return x.replace(".0", "")

    eda[1] = eda[1].apply(__format)
    eda = eda.rename(columns={0: "", 1: ""})

    return eda


def formatNumber(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


def build_eda_html(eda: pd.DataFrame, **kwargs):
    html = build_table(eda, color="grey_dark", **kwargs)
    with open("eda.html", "w") as f:
        f.write(html)


def get_number_of_nodes(G):
    return len(G.nodes())


def get_number_of_edges(G):
    return len(G.edges())


def get_average_degree(G):
    degrees = list(dict(G.degree()).values())
    average_degree = sum(degrees) / len(degrees)
    return round(average_degree)


def get_average_clustering(G):
    return nx.average_clustering(G)


def get_average_shortest_path(G):
    try:
        return nx.average_shortest_path_length(G)

    except nx.NetworkXError as error:
        if "Found infinite path length because the graph is not connected" in str(error):
            raise nx.NetworkXError("Graph is not connected use"
                                   "Ensure largest_component=True when"
                                   "initializing network")


def get_diameter(G):
    try:
        return nx.diameter(G)

    except nx.NetworkXError as error:
        if "Found infinite path length because the graph is not connected" in str(error):
            raise nx.NetworkXError("Graph is not connected use"
                                   "Ensure largest_component=True when"
                                   "initializing network")


def get_degree_centrality(G):
    return nx.degree_centrality(G)


def get_betweenness_centrality(G):
    return nx.betweenness_centrality(G)


def get_closeness_centrality(G):
    return nx.closeness_centrality(G)


def get_max_degree(G):
    return max(dict(G.degree).values())


def get_min_degree(G):
    return min(dict(G.degree).values())


if __name__ == "__main__":
    G0 = init_network(113500, 150000)
    eda_ = eda_caller(G0)
    a = extract_single_valued_statistics_to_dataframe(eda_)
    build_eda_html(a, font_family="monospace")
