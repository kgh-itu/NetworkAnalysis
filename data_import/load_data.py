import pandas as pd
from functools import lru_cache


@lru_cache()
def load_network_as_frame() -> pd.DataFrame:
    network_csv_path = "raw_data/edges.csv"
    col_map = {"# source": "source", " target": "target", " rssi": "rssi", " timestamp": "timestamp"}
    return pd.read_csv(network_csv_path).rename(columns=col_map)


if __name__ == "__main__":
    pass