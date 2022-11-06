import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import datetime

from data_import.load_data import select_data_between_timestamps
from EDA.Graphics.utils.tools import format_float_ticks
from EDA.Graphics.utils.style import custom_plot_style

save_fig_path = "EDA/Graphics/figures_pngs"


def plot_edge_count(start_timestamp=0, end_timestamp=np.inf, savefig=False):
    data = select_data_between_timestamps(start_timestamp, end_timestamp)
    data = data.groupby("timestamp")["source"].count()
    fig, ax = plt.subplots(figsize=(9, 4.8))
    custom_plot_style()
    ax.xaxis.set_major_formatter(FuncFormatter(format_float_ticks))
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("# Edges")
    ax.set_title("Edge Count at Timestamps for Network")
    ax.plot(data, c="#444444")
    if savefig:
        current_time = datetime.datetime.now().strftime("%d-%m-%Y%---%H:%M:%S")
        fig.savefig(f"{save_fig_path}/edge_count_from_{current_time}")

    plt.show()


if __name__ == "__main__":
    plot_edge_count(savefig=True)