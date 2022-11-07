import networkx as nx


def get_number_of_nodes(G):
    return len(G.nodes())


def get_number_of_edges(G):
    return len(G.edges())


def get_average_degree(G):
    degrees = list(dict(G.degree()).values())
    average_degree = sum(degrees) / len(degrees)
    return round(average_degree)


def get_average_clustering(G, **kwargs):
    return nx.average_clustering(G, **kwargs)


def get_average_shortest_path(G, **kwargs):
    try:
        return nx.average_shortest_path_length(G, **kwargs)

    except nx.NetworkXError as error:
        if "Graph is not connected" in str(error):
            raise nx.NetworkXError("Graph is not connected use"
                                   " get_largest_connected_component on G before calling.")


def get_diameter(G, **kwargs):
    try:
        return nx.diameter(G, **kwargs)

    except nx.NetworkXError as error:
        if "Found infinite path length because the graph is not connected" in str(error):
            raise nx.NetworkXError("Graph is not connected use"
                                   " get_largest_connected_component on G before calling.")


def get_degree_centrality(G):
    return nx.degree_centrality(G)


def get_betweenness_centrality(G, **kwargs):
    return nx.betweenness_centrality(G, **kwargs)


def get_closeness_centrality(G, **kwargs):
    return nx.closeness_centrality(G, **kwargs)
