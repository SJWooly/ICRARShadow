# A file for the combination of the text file edit, and xml > nx > json
# Aims to make the two files more condensed, and 'slick'
# 04/02/20


import networkx as nx
import xml.etree.ElementTree as et
from networkx.readwrite import json_graph
import json

diG = nx.DiGraph()
newListOfLines = []

def editUselessString(filename, searchString, replacementString):
    editedStrings = []
    with open(filename, 'r') as infile:
        for line in infile:
            if line.find(searchString) >= 0:
                editedStrings.append(replacementString)
            else:
               editedStrings.append(line)
    return editedStrings


newListOfLines = editUselessString('local_cybershake_100', 'xmlns', '<adag version="2.1" count="1" index="0" name="test" jobCount="25" fileCount="0" childCount="20">\n')

def replaceOldString(filename):
    with open(filename, 'w+') as outfile:
        for line in newListOfLines:
            outfile.write(line)


replaceOldString('edited_local_cybershake_100')

def addNodes(parsed_xml, diGNodes):
    root = parsed_xml.getroot()
    for job in root.findall('job'):
        job_id = job.get('id')
        runtime = job.get('runtime')  # variable names
        diGNodes.add_node(job_id, runtime=runtime)


addNodes(et.parse('edited_local_cybershake_100'), diG)


def addEdges(parsed_xml, diGEdges):
    root = parsed_xml.getroot()
    for child in root.findall('child'):
        v_edge = child.get('ref')
        for parent in root.iter('parent'):
            u_edge = parent.get('ref')
            diGEdges.add_edge(u_edge, v_edge)


addEdges(et.parse('edited_local_cybershake_100'), diG)


# converted_nx = json_graph.node_link_data(diG) # is this line necessary, can it be done in place in the one two down
with open("translated_local_cybershake_100.json", "w") as wfile:
    dumped_graph = json.dump(json_graph.node_link_data(diG), wfile, indent=4)
