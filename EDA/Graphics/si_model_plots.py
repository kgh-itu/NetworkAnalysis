import matplotlib.pyplot as plt

from Si_models.SI import epidemics
from EDA.Graphics.utils.style import custom_plot_style
from Network import init_network, get_timestamp_corresponding_to_day


def plot_si_for_different_betas(G, steps=200, title="", start_node=None):
    fig, ax = plt.subplots()
    custom_plot_style()
    ax.plot(epidemics(G, 0.1, steps=steps, start_node=start_node), label="Infection Rate=0.1")
    ax.plot(epidemics(G, 0.05, steps=steps, start_node=start_node), label="Infection Rate=0.05")
    ax.plot(epidemics(G, 0.025, steps=steps, start_node=start_node), label="Infection Rate=0.025")
    ax.plot(epidemics(G, 0.015, steps=steps, start_node=start_node), label="Infection Rate=0.015")
    ax.legend()
    ax.set_xlabel("Steps")
    ax.set_ylabel("Infected Ratio")
    ax.set_title(title)
    plt.show()


if __name__ == "__main__":
    monday_week1 = get_timestamp_corresponding_to_day(0)
    friday_week1 = get_timestamp_corresponding_to_day(4)
    G = init_network(*monday_week1)
    i_nodes = dict(G.degree())
    i_nodes = set([min(i_nodes, key=i_nodes.get)])
    plot_si_for_different_betas(G, title=f"Graph between timestamps {monday_week1}", start_node=i_nodes)
    G1 = init_network(*friday_week1)
    i_nodes = dict(G1.degree())
    i_nodes = set([min(i_nodes, key=i_nodes.get)])
    plot_si_for_different_betas(G1, title=f"Graph between timestamps {friday_week1}", start_node=i_nodes)

