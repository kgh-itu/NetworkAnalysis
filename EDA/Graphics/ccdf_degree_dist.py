import matplotlib.pyplot as plt
import pandas as pd
import datetime
from collections import Counter
import numpy as np
from scipy.stats import linregress

from scipy.optimize import curve_fit
import powerlaw

from EDA.Graphics.utils.style import custom_plot_style
from Network import init_network


def plot_ccdf(G, savefig=False) -> None:
    degree_count = get_degree_count(G)
    degree_count = degree_count.sort_values(by="degree", ascending=False)
    ccdf = calculate_ccdf(degree_count)
    ccdf = ccdf[["degree", "ccdf"]].sort_values(by="degree")
    ccdf = fit_line_to_ccdf(ccdf)
    fig, ax = _get_ax_and_fig(data=ccdf, x="degree", y="ccdf",
                              kind="line", loglog=True, c="#e41a1c",
                              label="CCDF")

    ax.plot(ccdf["degree"], ccdf["lin_reg_fit"], label="Fit")
    ax.legend()
    ax.set_xlabel("Degree")
    ax.set_ylabel("P(Degree >= x)")
    ax.set_title("CCDF (Complementary Cumulative Distribution Function)")
    plt.show()

    if savefig:
        current_time = datetime.datetime.now().strftime("%d-%m-%Y%---%H:%M:%S")
        fig.savefig(f"ccdf{current_time}.png")

    return ax


def plot_degree_distribution(G, loglog=False, savefig=False) -> None:
    degree_count = get_degree_count(G)
    degree_dist = degree_count.sort_values(by="degree")
    fig, ax = _get_ax_and_fig(data=degree_dist, x="degree",
                              kind="hist", loglog=loglog)

    ax.set_xlabel("Degree")
    ax.set_ylabel("Frequency")
    ax.set_title("Degree Distribution")
    plt.show()

    if savefig:
        current_time = datetime.datetime.now().strftime("%d-%m-%Y%---%H:%M:%S")
        fig.savefig(f"degree_distribution_{current_time}.png")


def fit_line_to_ccdf(ccdf):
    log_ccdf = np.log10(ccdf[["degree", "ccdf"]])
    slope, log10intercept, r_value, p_value, std_err = linregress(log_ccdf["degree"], log_ccdf["ccdf"])
    ccdf["lin_reg_fit"] = 10 ** log10intercept * ccdf["degree"]**slope
    return ccdf


def calculate_best_truncated_powerlaw_fit(ccdf):
    """Code is inspired by exercise 6.6."""

    def f(x, a, l):
        return (x ** a) * np.exp(l * x)

    def log_f(x, a, l):
        return np.log10(f(x, a, l))

    popt = curve_fit(log_f, ccdf["degree"], np.log10(ccdf["ccdf"]))[0]
    ccdf["fit"] = ccdf["degree"].apply(lambda x: f(x, popt[0], popt[1]))

    print(f"Optimal Parameters for fit: Alpha (a): {popt[0]}, Lambda (l): {popt[1]}")

    return ccdf


def fit_power_law(ccdf):
    results = powerlaw.Fit(ccdf["ccdf"])
    k_min = ccdf[ccdf["ccdf"] == results.power_law.xmin]["k"]
    print("Powerlaw CCDF Fit: %1.4f x ^ -%1.4f (k_min = %d)" % (
        10 ** results.power_law.Kappa, results.power_law.alpha, k_min))
    return


def get_degree_count(G) -> pd.DataFrame:
    degree_count = Counter(dict(G.degree).values())
    degree_count = pd.DataFrame(list(degree_count.items()), columns=("degree", "count"))
    return degree_count


def calculate_ccdf(data) -> pd.DataFrame:
    data["cum_sum"] = data["count"].cumsum()
    data["ccdf"] = data["cum_sum"] / data["count"].sum()
    return data


def _get_ax_and_fig(data, x, y=None, kind="scatter", loglog=False, c="#444444", **kwargs) -> (plt.Figure, plt.axes):
    fig, ax = plt.subplots(figsize=(9, 5))
    custom_plot_style()
    if kind == "line":
        ax.plot(x, y, data=data, c=c, **kwargs)
    elif kind == "hist":
        counts, bins = np.histogram(data[x])
        ax.hist(bins[:-1], bins, weights=counts, color=c, **kwargs)
        ax.tick_params(axis='y')
    if loglog:
        plt.yscale('log')
        plt.xscale('log')
    return fig, ax


if __name__ == "__main__":
    G_ = init_network(113500, 150000)
    plot_ccdf(G_)
