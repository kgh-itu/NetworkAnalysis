import networkx as nx
import pandas as pd

from Network import init_network
from pretty_html_table import build_table


def get_all_network_eda(G, eda_funcs=None) -> dict:
    EDA = {}
    if eda_funcs is None:
        eda_funcs = [get_number_of_nodes, get_number_of_edges, get_average_degree,
                     get_average_clustering, get_average_shortest_path,
                     get_diameter, get_max_degree, get_min_degree,
                     get_degree_centrality, get_betweenness_centrality, get_closeness_centrality]

    for func in eda_funcs:
        func(G, EDA)

    return EDA


def get_single_valued_eda_to_dataframe(eda) -> pd.DataFrame:
    """Gets all EDA with only 1 value for the entire graph into a dataframe
    Other eda that has to do with each node is not in output dataframe"""
    eda = {k: v for k, v in eda.items() if type(v) in [float, int]}
    eda = pd.DataFrame(eda.items())

    def __format(x):
        """very disgusting must be fixed"""
        x = round(x, 2)
        return str(x).replace(".0", "")

    eda[1] = eda[1].apply(__format)
    eda = eda.rename(columns={0: "", 1: ""})

    return eda


def build_eda_html(eda: pd.DataFrame, g, filename="eda.html", **kwargs):
    html = build_table(eda, color="grey_dark", **kwargs)
    html += f"<p style='font-family:monospace; font-size:15px; font-weight:normal'>" \
            f"Graph between timestamps ({g.start_timestamp}, {g.end_timestamp})" \
            f"</p>"
    with open(filename, "w") as f:
        f.write(html)


def get_number_of_nodes(G, eda):
    num_nodes = len(G.nodes())
    eda["# Nodes"] = num_nodes


def get_number_of_edges(G, eda):
    num_edges = len(G.edges())
    eda["# Edges"] = num_edges


def get_average_degree(G, eda):
    degrees = list(dict(G.degree()).values())
    average_degree = sum(degrees) / len(degrees)
    eda["Average Degree"] = average_degree


def get_average_clustering(G, eda):
    avg_clustering = nx.average_clustering(G)
    eda["Average Clustering"] = avg_clustering


def get_average_shortest_path(G, eda):
    try:
        average_shortest_path = nx.average_shortest_path_length(G)
        eda["Average Shortest Path"] = average_shortest_path

    except nx.NetworkXError as error:
        if "Found infinite path length because the graph is not connected" in str(error):
            raise nx.NetworkXError("Graph is not connected use"
                                   "Ensure largest_component=True when"
                                   "initializing network")


def get_diameter(G, eda):
    try:
        diameter = nx.diameter(G)
        eda["Diameter"] = diameter

    except nx.NetworkXError as error:
        if "Found infinite path length because the graph is not connected" in str(error):
            raise nx.NetworkXError("Graph is not connected use"
                                   "Ensure largest_component=True when"
                                   "initializing network")


def get_degree_centrality(G, eda):
    degree_centrality = nx.degree_centrality(G)
    eda["Degree Centrality"] = degree_centrality


def get_betweenness_centrality(G, eda):
    betweenness_centrality = nx.betweenness_centrality(G)
    eda["Betweenness Centrality"] = betweenness_centrality


def get_closeness_centrality(G, eda):
    closeness_centrality = nx.closeness_centrality(G)
    eda["Closeness Centrality"] = closeness_centrality


def get_max_degree(G, eda):
    max_degree = max(dict(G.degree).values())
    eda["Max Degree"] = max_degree


def get_min_degree(G, eda):
    min_degree = min(dict(G.degree).values())
    eda["Min Degree"] = min_degree


if __name__ == "__main__":
    G_ = init_network(113500, 150000)
    eda0 = get_all_network_eda(G_)
    eda1 = get_single_valued_eda_to_dataframe(eda0)
    build_eda_html(eda1, G_, font_family="monospace", width_dict=["500px", "500px"], font_size="15px")
