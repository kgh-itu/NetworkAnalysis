import seaborn


def custom_plot_style():
    style_dict = {'axes.edgecolor': '#444444',
                  "font.family": "monospace"}

    seaborn.set_theme(style="darkgrid", rc=style_dict)
