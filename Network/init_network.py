import networkx as nx
from data_import.load_data import load_network_as_frame
import numpy as np
from functools import lru_cache


def init_network(start_timestamp=0, end_timestamp=np.inf, largest_component=True) -> nx.Graph:
    data = load_network_as_frame()
    if end_timestamp == data["timestamp"].max():
        data = data.loc[(data["timestamp"] >= start_timestamp) & (data["timestamp"] <= end_timestamp)]
        end_timestamp = data["timestamp"].max()
    else:
        data = data.loc[(data["timestamp"] >= start_timestamp) & (data["timestamp"] < end_timestamp)]
        end_timestamp = data["timestamp"].max()

    G = nx.from_pandas_edgelist(data)
    if largest_component:
        G = _get_largest_connected_component(G)

    setattr(G, "start_timestamp", start_timestamp)
    setattr(G, "end_timestamp", end_timestamp)
    return G


def init_networks_for_all_days():
    all_graphs = [init_network(*get_timestamp_corresponding_to_day(i)) for i in range(28)]
    return all_graphs


def get_non_isolated_nodes_of_all_graphs(all_graphs):
    nodes = set()
    for graph in all_graphs:
        nodes_ = graph.nodes()
        for node in nodes_:
            nodes.add(node)

    return nodes


def _get_largest_connected_component(G):
    largest_component = max(nx.connected_components(G), key=len)
    return G.subgraph(largest_component)


def get_timestamp_corresponding_to_day(day=0):
    """28 total days: max timestamp is 2418900 -> 2418900/28 = 86389.28571428571"""
    start = 0
    end = 86389.28571428571

    start, end = 86389.28571428571 * day + start, 86389.28571428571 * day + end

    return start, end


if __name__ == "__main__":
    all_networks = init_networks_for_all_days()

