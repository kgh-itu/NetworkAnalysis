import random
from Network import init_networks_for_all_days, get_non_isolated_nodes_of_all_graphs, init_network


def epidemics(beta, start_node):
    all_graphs = init_networks_for_all_days()  # graph for each day in the period 28 total days
    total_node_count = len(get_non_isolated_nodes_of_all_graphs(all_graphs))  #
    G = all_graphs[0]  # first step at day 0
    if start_node:
        i_nodes = start_node
    else:
        i_nodes = set(random.sample(set(G.nodes), 1))
    s_at_any_time = set()
    i_sizes = []  # keep track of how the infected ratio grows for each step
    for i in range(len(all_graphs)):  # step for each day
        G = all_graphs[i]
        i_nodes = si(G, i_nodes, beta, s_at_any_time)
        i_sizes.append(len(i_nodes) / total_node_count)
    return i_sizes


def si(G, i_nodes, beta, s_at_any_time):
    new_infected = i_nodes.copy()
    current_infected_at_school = {node for node in new_infected if node in G}
    s_neighbors_of_i = {n for i_node in current_infected_at_school for n in G.neighbors(i_node)}
    for s_node in s_neighbors_of_i:
        s_at_any_time.add(s_node)
        if random.random() < beta:
            new_infected.add(s_node)

    return new_infected


def get_nodes_not_infected(infected_nodes):
    all_graphs = init_networks_for_all_days()
    all_nodes = get_non_isolated_nodes_of_all_graphs(all_graphs)

    return all_nodes.difference(infected_nodes)


if __name__ == "__main__":
    infected_ratio, infected_nodes = epidemics(1, start_at_highest_degree=True)
    print(infected_ratio[-1])
    print(get_nodes_not_infected(infected_nodes))

