import networkx as nx
from data_import.load_data import select_data_between_timestamps
import numpy as np


def init_network(start_timestamp=0, end_timestamp=np.inf):
    data = select_data_between_timestamps(start_timestamp, end_timestamp)
    return nx.from_pandas_edgelist(data)


if __name__ == "__main__":
    G = init_network()
