# A file for shell code to execute the 'CombinedEitAndTranslate' functions
# Currently aims to work on the cybershake xml examples
# 04/02/20

import xml.etree.ElementTree as et
from networkx.readwrite import json_graph
import json
import networkx as nx
from ShellVerEditAndTranslate import editUselessString, replaceOldString, addNodes, addEdges

diG = nx.DiGraph()
listOfLines = editUselessString('local_cybershake_100', 'xmlns',
                                '<adag version="2.1" count="1" index="0" name="test" jobCount="25" fileCount="0" childCount="20">\n')

editUselessString('local_cybershake_100',
                        'xmlns', '<adag version="2.1" count="1" index="0" name="test" jobCount="25" fileCount="0" childCount="20">\n')

replaceOldString('local_cybershake_100')

addNodes(et.parse('edited_local_cybershake_100'), diG)

addEdges(et.parse('edited_local_cybershake_100'), diG)

converted_nx = json_graph.node_link_data(diG)  # root label?
with open("shell_translated_local_cybershake_100.json", "w") as wfile:
    dumped_graph = json.dump(converted_nx, wfile, indent=4)