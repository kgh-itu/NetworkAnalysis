import networkx as nx
from data_import.load_data import select_network_between_timestamps
import numpy as np


def init_network(start_timestamp=0, end_timestamp=np.inf, largest_component=True) -> nx.Graph:
    data = select_network_between_timestamps(start_timestamp=start_timestamp,
                                             end_timestamp=end_timestamp)
    G = nx.from_pandas_edgelist(data)
    if largest_component:
        return get_largest_connected_component(G)

    return G


def get_largest_connected_component(G):
    largest_component = max(nx.connected_components(G), key=len)
    return G.subgraph(largest_component)


if __name__ == "__main__":
    G0 = init_network(113500, 150000, largest_component=False)
    G1 = get_largest_connected_component(G0)

