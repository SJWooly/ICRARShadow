# A sample graph using the previously dictated 'shadow'
# infrastructure to draft the construction of a graph from xml
# version: 07/01/20

import networkx as nx
import matplotlib.pyplot as plt
import xml.etree.ElementTree as et

diG = nx.DiGraph()
tree = et.parse('/home/sarah/Desktop/country_data') #need to re-specify location
# @TODO construct checked exception ffor event of non-existent file
root = tree.getroot()
print(root)

def addNodes(diGNodes):
    print(root)


addNodes(diG)



# nx.draw(diG, with_labels=True, font_weight='bold')
# plt.show()