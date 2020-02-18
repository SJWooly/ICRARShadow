import unittest
from EditAndTranslate import clean_xml, build_dag


class TranslatorTestCase(unittest.TestCase):
	def test_bothEndsOfEdge(self):
		edge_u, edge_v = None, None
		self.assertNotEqual(edge_u, edge_v, msg="Edge cannot start and end at the same node")
		pass

	def test_allNodesConnected(self):
		# determine how to test
		pass

	def test_acyclicGraph(self):
		# parent and child combination are not also a child and parent
		# ie edge does not go both ways
		pass

	def test_NodesExist(self):
		pass

	def test_EdgesExist(self):
		pass


if __name__ == '__main__':
	unittest.main()
