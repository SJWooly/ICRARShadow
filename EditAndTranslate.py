# A file for the combination of the text file edit, and xml > nx > json
# Aims to make the two files more condensed, and 'slick'
# 04/02/20


import networkx as nx
import sys
# allows for removal of string which interferes with etree

def clean_xml(filename, newfile, search_str, replacement_str):
	edited_str_lines = []
	with open(filename, 'r') as infile:
		for line in infile:
			# output of searchString method is the index of said str or
			# -1 if the search_str is not present
			if line.find(search_str) >= 0:
				edited_str_lines.append(replacement_str)
			else:
				edited_str_lines.append(line)
	with open(newfile, 'w+') as outfile:
		for line in edited_str_lines:
			outfile.write(line)


# adds edges to the building DAG
def build_dag(parsed_xml):
	building_dag = nx.DiGraph()
	parsed_xml = et.parse(xml)
	root = parsed_xml.getroot()
	for child in root.findall("child"):
		id = child.get('ref')
		for parent in child.findall("parent"):
			pid = parent.get('ref')
			building_dag.add_edge(pid, id)
	for node in building_dag.nodes:
		runtime = [e.get('runtime') for e in root.findall("job/[@id='{0}']".format(node))]
		building_dag.nodes[node]['comp'] = float(runtime[0])
		x = node

	for edge in building_dag.edges:
		output = [e.get('file') for e in
				  root.findall("job/[@id='{0}']/uses/[@link='output'][@file]".format(edge[0]))]
		input = [e.get('file') for e in root.findall("job/[@id='{0}']/uses/[@link='input'][@file]".format(edge[1]))]
		sout = set(output)
		sinput = set(input)
		intersect_file = (sout & sinput)
		# CYBERSHAKE DOES SOMETHING DIFFERENT HERE (DON'T ASK ME WHY)
		if len(intersect_file) == 0:
			building_dag.edges[edge]['size'] = float(0)
		elif len(intersect_file) > 0:
			# Loop through each of the intersect files and add up the cumulative data
			total = 0
			for file in intersect_file:
				element = root.findall("job/[@id='{0}']/uses/[@link='output'][@file='{1}']".format(edge[0], file))
				total += float(element[0].get('size'))
			building_dag.edges[edge]['size'] = total
		else:
			sys.exit("Issues translating DAX")

	return building_dag
if __name__ == '__main__':
	import xml.etree.ElementTree as et
	from networkx.readwrite import json_graph
	import json

	# reoves the unnecessary string (passed as parameter and outputs an edited file)
	clean_xml('HEFT_paper.xml', 'edited_HEFT_paper.xml', 'xmlns',
			  '<adag version="2.1" count="1" index="0" name="test" jobCount="25" fileCount="0" childCount="20">\n')

	# adds nodes and edges from the edited xml to the nx DAG
	finished_dag = build_dag(et.parse('edited_HEFT_paper.xml'))

	# dumps the complete DAG from nx into json, now translated and ready for use
	with open("translated_edited_" + "HEFT_paper" + ".json", "w") as wfile:
		dumped_graph = json.dump(json_graph.node_link_data(finished_dag), wfile, indent=4)
