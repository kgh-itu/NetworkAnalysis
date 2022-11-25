import matplotlib.pyplot as plt

from Si_models.SI import epidemics
from EDA.Graphics.utils.style import custom_plot_style
from Network import init_network, get_timestamp_corresponding_to_day


def plot_si_for_different_betas(title="", start_at_highest_degree=True):
    fig, ax = plt.subplots(figsize=(10, 6))
    custom_plot_style()
    tmp0 = epidemics(0.1, start_at_highest_degree=False)
    tmp1 = epidemics(0.1, start_at_highest_degree=True)
    ax.plot(tmp0[0], label="Infection Rate=1, Random Start")
    ax.plot(tmp1[0], label="Infection Rate=1, Highest Degree Start")
    ax.legend()
    ax.set_xlabel("Days")
    ax.set_ylabel("Infected Ratio")
    ax.set_title(title)
    plt.show()


if __name__ == "__main__":
    plot_si_for_different_betas()

