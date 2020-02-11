# A file for shell code to execute the 'EditAndTranslate' functions
# Currently aims to work on the cybershake xml examples, and eventually the HEFT_paper etc
# February 2020

import xml.etree.ElementTree as et
from networkx.readwrite import json_graph
import json
from EditAndTranslate import editUselessString, replaceOldString, addNodes, addEdges

# finds the useless (bug causing namespace) string, puts the edited set of strings into listOfLines
listOfLines = editUselessString('HEFT_paper.xml', 'xmlns',
                                '<adag version="2.1" count="1" index="0" name="test" jobCount="25" fileCount="0" childCount="20">\n')

# puts the listOfLines into a new file, ready to be utilised
replaceOldString('edited_' + 'HEFT_paper.xml', listOfLines)

#adds the nodes from the edited xml to the nx DAG
buildingDiG = addNodes(et.parse('edited_' + 'HEFT_paper.xml'))

#adds the edges from the edited xml to the nx DAG
diGComplete = addEdges(et.parse('edited_' + 'HEFT_paper.xml'), buildingDiG)

#dumps the complete DAG from nx into json, now translated and ready for use
with open("translated_edited_" + "HEFT_paper" + ".json", "w") as wfile:
    dumped_graph = json.dump(json_graph.node_link_data(diGComplete), wfile, indent=4)
