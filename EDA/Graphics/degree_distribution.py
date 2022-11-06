import matplotlib.pyplot as plt
import pandas as pd
import datetime
from collections import Counter

from EDA.Graphics.utils.style import custom_plot_style
from network.init_network import init_network

save_fig_path = "EDA/Graphics/figures_pngs"


def plot_ccdf(G, savefig=False) -> None:
    degree_count = get_degree_count(G)
    ccdf = degree_count.sort_values(by="degree", ascending=False)
    ccdf["cum_sum"] = ccdf["count"].cumsum()
    ccdf["prob"] = ccdf["cum_sum"] / ccdf["count"].sum()
    ccdf = ccdf[["degree", "prob"]].sort_values(by="degree")
    fig, ax = _get_ax_and_fig(data=ccdf, x="degree", y="prob",
                              kind="line", loglog=True)
    ax.set_xlabel("Degree")
    ax.set_ylabel("P(Degree > x)")
    ax.set_title("CCDF (Complementary Cumulative Distribution Function)")
    plt.show()

    if savefig:
        current_time = datetime.datetime.now().strftime("%d-%m-%Y%---%H:%M:%S")
        fig.savefig(f"{save_fig_path}/ccdf_{current_time}.png")


def plot_degree_distribution(G, loglog=False, savefig=False) -> None:
    degree_count = get_degree_count(G)
    degree_dist = degree_count.sort_values(by="degree")
    fig, ax = _get_ax_and_fig(data=degree_dist, x="degree", y="count",
                              kind="scatter", loglog=loglog)
    ax.set_xlabel("Degree")
    ax.set_ylabel("Count")
    ax.set_title("Degree Distribution")
    plt.show()

    if savefig:
        current_time = datetime.datetime.now().strftime("%d-%m-%Y%---%H:%M:%S")
        fig.savefig(f"{save_fig_path}/degree_distribution_{current_time}.png")


def get_degree_count(G) -> pd.DataFrame:
    degree_count = Counter(dict(G.degree).values())
    degree_count = pd.DataFrame(list(degree_count.items()), columns=("degree", "count"))
    return degree_count


def _get_ax_and_fig(data, x, y, kind="scatter", loglog=False) -> (plt.Figure, plt.axes):
    fig, ax = plt.subplots(figsize=(9, 4.8))
    custom_plot_style()
    if kind == "line":
        ax.plot(x, y, data=data, c="#444444")
    elif kind == "scatter":
        ax.scatter(x, y, data=data, c="#444444")
    if loglog:
        ax.set_yscale('log')
        ax.set_xscale('log')

    return fig, ax


if __name__ == "__main__":
    G_ = init_network()
    plot_ccdf(G_, savefig=False)
    plot_degree_distribution(G_, savefig=False, loglog=False)
