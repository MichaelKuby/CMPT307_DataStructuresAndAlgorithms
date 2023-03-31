# Write two programs for Prim’s minimum spanning tree algorithm discussed in class, one implements the algorithm
# with the input graph G represented by adjacency list and the other implements the algorithm with G represented
# by adjacent matrix.

import networkx as nx
import numpy as np
from timeit import default_timer as timer

from prims import prims_list, prims_matrix
import random as rand

def create_graph(n, m):
    # n = number of nodes ... m = number of edges
    # Returns a graph G

    # Create a random tree of size n. It will have m = n-1 edges
    G = nx.random_tree(n)

    # Add a random weight to each edge
    for u, v in nx.edges(G):
        x = rand.randint(1, 100)
        G[u][v]["weight"] = x

    # Add up to m more edges
    m = m - (n-1)
    while m >= 0:
        u = rand.randint(0, n-1)
        v = rand.randint(0, n-1)
        if u != v:
            x = rand.randint(1, 100)
            G.add_edge(u, v)
            G[u][v]["weight"] = x
            m = m-1

    return G

def create_adjacency_matrix(G):
    n = nx.number_of_nodes(G)
    m = np.zeros((n, n))
    for u, v in nx.edges(G):
        m[u][v] = G[u][v]["weight"]
        m[v][u] = G[u][v]["weight"]
    return m

def main():

    """# Create the input graph G represented by an adjacency list
    G = nx.Graph()

    G.add_edge(0, 1, weight=4)
    G.add_edge(0, 7, weight=8)
    G.add_edge(1, 2, weight=8)
    G.add_edge(1, 7, weight=11)
    G.add_edge(2, 8, weight=2)
    G.add_edge(2, 3, weight=7)
    G.add_edge(2, 5, weight=4)
    G.add_edge(3, 4, weight=9)
    G.add_edge(3, 5, weight=14)
    G.add_edge(4, 5, weight=10)
    G.add_edge(5, 6, weight=2)
    G.add_edge(6, 7, weight=1)
    G.add_edge(6, 8, weight=6)
    G.add_edge(7, 8, weight=7)

    G, A = prims_list(G, 1)
    m = create_adjacency_matrix(G)
    G, A = prims_matrix(G, m, 0)

    cost = 0
    for u, v in A:
        x = G[u][v]['weight']
        cost = cost + x
    print(cost)
    print(A)"""


    n = [100, 200, 400, 800]

    for q in n:
        m = [3 * q, q ** 1.5, (q * (q - 1)) / 2]
        for t in m:
            G = create_graph(q, t)
            matrix = nx.to_numpy_array(G)

            # List
            start = timer()
            prims_list(G, 0)
            end = timer()
            print("Adjacency List. n = " + str(q) + ", m = " + str(t) + "- Run time: " + str(end - start) + ".")

            # Matrix
            start = timer()
            prims_matrix(G, matrix, 0)
            end = timer()
            print("Adjacency Matrix. n = " + str(q) + ", m = " + str(t) + "- Run time: " + str(end - start) + ".")

    """print(sorted(A))
    print(len(A))

    costA = 0
    for u, v in A:
        x = G[u][v]['weight']
        costA = costA + x
    print(costA)"""



    """print(sorted(B))
    print(len(B))

    costB = 0
    for u, v in B:
        x = G[u][v]['weight']
        costB = costB + x
    print(costB)"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
