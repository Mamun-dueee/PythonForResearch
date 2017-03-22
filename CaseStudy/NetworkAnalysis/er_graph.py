import networkx as nx
from scipy.stats import bernoulli

def er_graph(N, p):
    """Generate an ER graph"""
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
	    if node1 < node2 and bernoulli.rvs(p = p):
		G.add_edge(node1, node2)
    return G
