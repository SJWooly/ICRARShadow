import networkx as nx
import xml.etree.ElementTree as et
from networkx.readwrite import json_graph
import json

diG = nx.DiGraph()
tree = et.parse('/home/sarah/Desktop/local_cybershake_100_noNS')  # need to re-specify location
# @TODO error ffor event of non-existent file
# @TODO error iff nodes andd/orr edges iss empty
# @TODO specify the graph overview iff xml has that data top


# def removeNameSpaces(sample_tree)

def addNodes(diGNodes):
    root = tree.getroot()
    for job in root.findall('job'):
        job_id = job.get('id')
        runtime = job.get('runtime')  # variable names
        diGNodes.add_node(job_id, runtime=runtime)


addNodes(diG)


def addEdges(diGEdges):
    root = tree.getroot()
    for child in root.findall('child'):
        v_edge = child.get('ref')
        for parent in root.iter('parent'):
            u_edge = parent.get('ref')

            diGEdges.add_edge(u_edge, v_edge)


addEdges(diG)

converted_nx = json_graph.node_link_data(diG)  # root label?
with open("temp_data.json", "w") as wfile:
    dumped_graph = json.dump(converted_nx, wfile, indent=4)
