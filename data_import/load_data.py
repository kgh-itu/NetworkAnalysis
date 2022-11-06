import pandas as pd
import numpy as np


def select_network_between_timestamps(start_timestamp=0, end_timestamp=np.inf) -> pd.DataFrame:
    data = load_network_as_frame()
    return data.loc[(data["timestamp"] >= start_timestamp) & (data["timestamp"] <= end_timestamp)]


def load_network_as_frame() -> pd.DataFrame:
    network_csv_path = "raw_data/edges.csv"
    col_map = {"# source": "source", " target": "target", " rssi": "rssi", " timestamp": "timestamp"}
    return pd.read_csv(network_csv_path).rename(columns=col_map)


if __name__ == "__main__":
    data_ = select_network_between_timestamps(0,  10000)