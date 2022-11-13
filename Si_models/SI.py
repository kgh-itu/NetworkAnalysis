import random


def epidemics(G, beta, steps, start_node=None):
    if start_node is None:
        i_nodes = set(random.sample(set(G.nodes), 1))
    else:
        i_nodes = start_node
    i_sizes = [1 / len(G.nodes), ]
    for _ in range(steps):
        i_nodes = si(G, i_nodes, beta)
        i_sizes.append(len(i_nodes) / len(G.nodes))
    return i_sizes


def si(G, i_nodes, beta):
    new_infected = i_nodes.copy()
    s_neighbors_of_i = {n for i_node in i_nodes for n in G.neighbors(i_node)}
    for s_node in s_neighbors_of_i:
        if random.random() < beta:
            new_infected.add(s_node)
    return new_infected
