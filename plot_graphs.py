import networkx as nx

import numpy as np

import matplotlib.pyplot as plt


def skeleton(graph):
    skeleton = np.copy(graph + graph.transpose())
    return (skeleton > 0).astype('bool').astype('int')


def plot_graphs(true_graph, estimated_graph):
    # Plot true graph
    G = nx.DiGraph(true_graph)
    fig = plt.figure(figsize=(6, 2))
    ax = fig.add_subplot(141)
    nx.draw(G, fig=fig, ax=ax, node_color='orange', 
        labels = dict([(i, i) for i in range(len(true_graph))]),
        # edge_color=edge_color,
        node_size=150,
        width=3.,
        font_size=10,
        pos=nx.circular_layout(G),
        )
    ax.set_title("True", fontsize=8)

    # Plot skeleton results
    G = nx.Graph(skeleton(true_graph) | (estimated_graph))
    edge_color = []
    for ij in G.edges():
        # print ij, skeleton(true)[ij], skeleton(estimated)[ij]
        if skeleton(true_graph)[ij] == 1 and skeleton(estimated_graph)[ij] == 1:
            edge_color.append('black')
        elif skeleton(true_graph)[ij] == 1 and skeleton(estimated_graph)[ij] == 0:
            edge_color.append('red')
        elif skeleton(true_graph)[ij] == 0 and skeleton(estimated_graph)[ij] == 1:
            edge_color.append('grey')

    # fig = plt.figure(figsize=(6, 2))
    ax = fig.add_subplot(122)
    nx.draw(G, fig=fig, ax=ax, node_color='orange', 
        labels = dict([(i, i) for i in range(len(true_graph))]),
        edge_color=edge_color,
        node_size=150,
        width=3.,
        font_size=10,
        pos=nx.circular_layout(G),
        )
    ax.set_title("Skeleton", fontsize=8)
    fig.suptitle("Model", x=0, fontsize=12, horizontalalignment='left')