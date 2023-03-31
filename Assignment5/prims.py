import networkx as nx
import heapdict

def prims_list(G, r):
    A = []
    nx.set_node_attributes(G, float('inf'), 'key')
    nx.set_node_attributes(G, None, 'pi')
    nx.set_node_attributes(G, 1, 'queued')
    G.nodes[r]["key"] = 0
    Q = heapdict.heapdict()
    for u in G.nodes:
        Q[u] = G.nodes[u]["key"]
    while Q:
        u, key = Q.popitem()
        G.nodes[u]['queued'] = 0 # add u to the tree
        if G.nodes[u]["pi"] != None:
            A.append((G.nodes[u]["pi"], u))
        for v in nx.neighbors(G, u):
            if (G.nodes[v]['queued'] == 1) and (G[u][v]["weight"] < G.nodes[v]["key"]):
                G.nodes[v]["pi"] = u
                G.nodes[v]["key"] = G[u][v]["weight"]
                Q[v] = G[u][v]["weight"]
    return G, A

def prims_matrix(G, m, r):
    # Create the set of edges of the tree
    A = []

    # Set attributes
    nx.set_node_attributes(G, float('inf'), 'key')
    nx.set_node_attributes(G, None, 'pi')
    nx.set_node_attributes(G, 1, 'queued')
    G.nodes[r]["key"] = 0
    n = m.shape[0]

    # Create and fill the Queue
    Q = heapdict.heapdict()
    for u in G.nodes:
        Q[u] = G.nodes[u]["key"]
    while Q:
        u, key = Q.popitem()
        G.nodes[u]['queued'] = 0  # add u to the tree
        if G.nodes[u]["pi"] != None:
            A.append((G.nodes[u]["pi"], u))
        for i in range(n):
            if G.nodes[i]['queued'] == 0: # Check only those nodes that are part of the tree
                for j in range(n): # Check each column of those rows (nodes)
                    if i != j and m[i][j] > 0 and G.nodes[j]['queued'] == 1 and m[i][j] < G.nodes[j]["key"]:
                        G.nodes[j]["pi"] = i
                        G.nodes[j]["key"] = m[i][j]
                        Q[j] = m[i][j]
    return G, A