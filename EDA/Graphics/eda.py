import pandas as pd
from functools import lru_cache
import matplotlib.pyplot as plt
from EDA.Graphics.utils.style import custom_plot_style


@lru_cache
def plot_edas():
    eda = pd.read_csv("eda.csv")
    eda = eda.drop(columns="Unnamed: 0")

    eda["color"] = [0, 1, 2, 3, 4, 5, 6] * 4
    print(eda)

    for i, col in enumerate(list(eda.columns)[0:-1]):
        fig, ax = plt.subplots(figsize=(11, 6))
        custom_plot_style(style="whitegrid")
        scatter = ax.scatter(eda.index, eda[col], c=eda["color"], zorder=2, cmap="tab10")
        ax.plot(eda[col], 'gray', zorder=1, linestyle="dashed")
        ax.set_xlabel("Days")
        ax.set_ylabel(col)
        ax.set_title(f"{col} Over 28 Days")
        ax.legend(handles=scatter.legend_elements()[0], labels=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
                  fancybox=False, shadow=True, bbox_to_anchor=(1, 1))

        plt.savefig(f"{col}_EDA")
        plt.show()

    return eda

if __name__ == "__main__":
    eda = plot_edas()
