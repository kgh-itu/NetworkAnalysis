from networkx import betweenness_centrality, degree_centrality, closeness_centrality, eigenvector_centrality
from Si_models.SI import epidemics
from Network.init_network import init_networks_for_all_days, get_non_isolated_nodes_of_all_graphs
import time
import pickle
import numpy as np
import matplotlib.pyplot as plt
from EDA.Graphics.utils.style import custom_plot_style
import random

np.random.seed(42)

# finding start nodes with the highest degree, betweenness, closeness centrality etc.


start_time = time.time()
all_G = init_networks_for_all_days()
all_nodes = get_non_isolated_nodes_of_all_graphs(all_G)

with open('betweenness_c.pickle', 'rb') as handle:
    betweenness_c = pickle.load(handle)

with open('closeness_c.pickle', 'rb') as handle:
    closeness_c = pickle.load(handle)

with open('degree_c.pickle', 'rb') as handle:
    degree_c = pickle.load(handle)

with open('eigenvector_c.pickle', 'rb') as handle:
    eigenvector_c = pickle.load(handle)

avg_betweenness_c = {k: np.mean(value) for k, value in betweenness_c.items()}
avg_closeness_c = {k: np.mean(value) for k, value in closeness_c.items()}
avg_degree_c = {k: np.mean(value) for k, value in degree_c.items()}
eigenvector_c = {k: np.mean(value) for k, value in eigenvector_c.items()}

avg_degree_c[51]

days_active_per_node = {k: len(value) for k, value in betweenness_c.items()}

nodes_active_28_days = {k: v for k, v in days_active_per_node.items() if v == 28}
nodes_active_13_days = {k: v for k, v in days_active_per_node.items() if v == 13}

avg_degree_c_active_28_days = {k: avg_degree_c[k] for k in nodes_active_28_days.keys()}
min_28 = min(avg_degree_c_active_28_days.keys(), key=(lambda k: avg_degree_c_active_28_days[k]))  # 332
max_28 = max(avg_degree_c_active_28_days.keys(), key=(lambda k: avg_degree_c_active_28_days[k]))  # 51

avg_degree_c_active_13_days = {k: avg_degree_c[k] for k in nodes_active_13_days.keys()}
min_13 = min(avg_degree_c_active_13_days.keys(), key=(lambda k: avg_degree_c_active_13_days[k]))  # 579
max_13 = max(avg_degree_c_active_13_days.keys(), key=(lambda k: avg_degree_c_active_13_days[k]))  # 544

# avg_closeness_max_node = max(avg_closeness_c, key=avg_closeness_c.get)
# avg_closeness_max_node_value = avg_closeness_c[avg_closeness_max_node]
# days_active_max_closeness_degree = days_active_per_node[avg_closeness_max_node]
#
# avg_betweenness_max_node = max(avg_betweenness_c, key=avg_degree_c.get)
# avg_betweenness_max_node_value = avg_betweenness_c[avg_betweenness_max_node]
# days_active_max_betweenness_degree = days_active_per_node[avg_betweenness_max_node]
#
# avg_degree_max_node = max(avg_degree_c, key=avg_degree_c.get)  # 544
# avg_degree_max_node_value = avg_degree_c[avg_degree_max_node]
# days_active_max_avg_degree = days_active_per_node[avg_degree_max_node]

N = 50
BETA = 0.15
si_active_28_days_highest_degree = np.zeros(len(all_G))
for i in range(N):
    si_active_28_days_highest_degree += np.array(epidemics(BETA, set([max_28])))

si_active_28_days_highest_degree = si_active_28_days_highest_degree / N

si_active_28_days_lowest_degree = np.zeros(len(all_G))
for i in range(N):
    si_active_28_days_lowest_degree += np.array(epidemics(BETA, set([min_28])))

si_active_28_days_lowest_degree = si_active_28_days_lowest_degree / N

si_highest_overall_degree_c = np.zeros(len(all_G))
for i in range(N):
    si_highest_overall_degree_c += np.array(epidemics(BETA, set([max_13])))

si_highest_overall_degree_c = si_highest_overall_degree_c / N

si_lowest_13_degree_c = np.zeros(len(all_G))
for i in range(N):
    si_lowest_13_degree_c += np.array(epidemics(BETA, set([min_13])))

si_lowest_13_degree_c = si_lowest_13_degree_c / N

fig, ax = plt.subplots(figsize=(11, 6))
custom_plot_style()
ax.plot(si_active_28_days_highest_degree)
ax.plot(si_active_28_days_lowest_degree)
ax.plot(si_highest_overall_degree_c)
ax.plot(si_lowest_13_degree_c)
ax.legend(['H (28 days)', 'L (28 days)', 'H Overall (13 days)', 'L (13 days)'])
ax.set_title(F"SI beta = {BETA}")
ax.set_xlabel("Days/Steps")
ax.set_ylabel("Infected Ratio")
plt.show()






# node: 544 highest degree centrality
# node:

# det er 2 ting der påvirker smitten. 1) hvor mange dage en node er aktiv og hvor mange andre den kan smitte på en
# given dag.

# closeness_c = {i: [] for i in girt all_nodes}
# degree_c = {i: [] for i in all_nodes}
# betweenness_c = {i: [] for i in all_nodes}
#
# for G in all_G:
#     btw_c = betweenness_centrality(G)
#     for key, value in btw_c.items():
#         betweenness_c[key].append(value)
#
# for G in all_G:
#     deg_c = degree_centrality(G)
#     for key, value in deg_c.items():
#         degree_c[key].append(value)
#
# for G in all_G:
#     clo_c = closeness_centrality(G)
#     for key, value in clo_c.items():
#         closeness_c[key].append(value)

# for G in all_G:
# btw_c = eigenvector_centrality(G)
# for key, value in btw_c.items():
#     eigenvector_c[key].append(value)
# over 20 dage
