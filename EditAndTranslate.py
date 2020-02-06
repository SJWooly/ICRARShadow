# A file for the combination of the text file edit, and xml > nx > json
# Aims to make the two files more condensed, and 'slick'
# 04/02/20


import networkx as nx


# allows for removal of string which interferes with etree
def editUselessString(filename, searchString, replacementString):
    with open(filename, 'r') as infile:
        editedStrings = []
        for line in infile:
            if line.find(searchString) >= 0:
                editedStrings.append(replacementString)
            else:
               editedStrings.append(line)
    return editedStrings


# replaces removed string with only the relevant contents of that line
def replaceOldString(filename, listOfLines):
    with open(filename, 'w+') as outfile:
        for line in listOfLines:
            outfile.write(line)

#adds nodes to the building DAG
def addNodes(parsed_xml,):
    buildingDiG = nx.DiGraph()
    root = parsed_xml.getroot()
    for job in root.findall('job'):
        job_id = job.get('id')
        runtime = job.get('runtime')  # variable names
        buildingDiG.add_node(job_id, comp=runtime) #check variable name here
    return buildingDiG

#adds edges to the building DAG
def addEdges(parsed_xml, buildingDiG):
    root = parsed_xml.getroot()
    for child in root.findall('child'):
        v_edge = child.get('ref')
        for parent in root.iter('parent'):
            u_edge = parent.get('ref')
            buildingDiG.add_edge(u_edge, v_edge)
    return buildingDiG

