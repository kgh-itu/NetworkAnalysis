import matplotlib.pyplot as plt

from Si_models.SI import epidemics
from EDA.Graphics.utils.style import custom_plot_style
from Network import init_network, get_timestamp_corresponding_to_day


def plot_si_for_different_betas(title="", start_at_highest_degree=True):
    fig, ax = plt.subplots(figsize=(10, 6))
    custom_plot_style()
    ax.plot(epidemics(0.2, start_at_highest_degree)[0], label="Infection Rate=0.2")
    ax.plot(epidemics(0.1, start_at_highest_degree)[0], label="Infection Rate=0.1")
    ax.plot(epidemics(0.05, start_at_highest_degree)[0], label="Infection Rate=0.05")
    ax.plot(epidemics(0.025, start_at_highest_degree)[0], label="Infection Rate=0.025")
    ax.legend()
    ax.set_xlabel("Days")
    ax.set_ylabel("Infected Ratio")
    ax.set_title(title)
    plt.show()


if __name__ == "__main__":
    plot_si_for_different_betas()

