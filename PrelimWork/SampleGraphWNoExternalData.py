# A sample graph using the previously dictated 'shadow'
# infrastructure to construct a simple graph
# version: 07/01/20


import networkx as nx
import matplotlib.pyplot as plt


di = nx.DiGraph()
nodes = [0, 1, 2, 3]
compValues = [10, 11, 12, 13]
edges = [(1, 0), (2, 1), (2, 0), (2, 3), (1, 3), (0, 3)]
edgeWeights = [20, 21, 22, 23, 24, 25]


# current structure assumes all elements are in separate lists
# @TODO reformat depending on how accessing data from xml

# @TODO how to access compvalue
def addNodes(diGraphNodes, localNodes, localCompValues):
    for node in nodes:
        if not nodes or not compValues:
            break
        else:
            diGraphNodes.add_node(node, comp = compValues[nodes.index(node)])



def addEdges(diGraphEdges, localEdges, localEdgeWeights):
    for edge in edges:
        if not edges or not edgeWeights:
            break
        else:
            diGraphEdges.add_edge(edge[0],edge[1], weight = localEdgeWeights[edges.index(edge)])



addNodes(di, nodes, compValues)
addEdges(di, edges, edgeWeights)



nx.draw(di, with_labels=True, font_weight='bold')
plt.show()
