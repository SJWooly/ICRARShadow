# A file for the combination of the text file edit, and xml > nx > json
# Aims to make the two files more condensed, and 'slick'
# 04/02/20


import networkx as nx

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
def build_dag(parsed_xml, building_dag):
	building_dag = nx.DiGraph()
	root = parsed_xml.getroot()
	for job in root.findall('job'):
		job_id = job.get('id')
		runtime = job.get('runtime')
		building_dag.add_node(job_id, comp=runtime)

	for child in root.findall('child'):
		v_edge = child.get('ref')
		for parent in root.iter('parent'):
			u_edge = parent.get('ref')
			# makes node IDs into ints, by ignoring the ID prefix
			num_v_edge = int(v_edge[2:])
			num_u_edge = int(u_edge[2:])
			# this may be more efficient through a swap variable
			# format of edge naming is heft_file_"lower_node_ID"_"upper_node_ID"
			if num_u_edge < num_v_edge:
				lower_node = num_u_edge
				upper_node = num_v_edge
			else:
				lower_node = num_v_edge
				upper_node = num_u_edge
			for use in root.iter('uses'):
				edge_use = use.get('file')
				if edge_use == "heft_file_" + str(lower_node) + "_" + str(upper_node):
					size = use.get('size')
		building_dag.add_edge(u_edge, v_edge, data_size=size)
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
