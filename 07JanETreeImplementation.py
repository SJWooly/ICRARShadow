import networkx as nx
import matplotlib.pyplot as plt
import xml.etree.ElementTree as et

diG = nx.DiGraph()
tree = et.parse('/home/sarah/Desktop/country_data') #need to re-specify location
# @TODO construct checked exception ffor event of non-existent file


def addNodes(diGNodes):
    root = tree.getroot()
    for country in root.findall('country'):
        id = country.get('name')
        gdp = country.find('gdppc').text
        diGNodes.add_node(id, gdp=gdp)

addNodes(diG)


def addEdges(diGEdges):
    root = tree.getroot()
    for id in root:
        z = country.find('computational_weight').text
        if xy:
            diGEdges.add_edge(a, b, weight=z)


# addEdges(diG)


# nx.draw(diG, with_labels=True, font_weight='bold')
# plt.show()
# see for json dump https://networkx.github.io/documentation/stable/reference/readwrite/generated/networkx.readwrite.json_graph.node_link_data.html