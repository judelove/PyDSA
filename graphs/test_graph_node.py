from unittest import TestCase

from graphs.graph import Graph
from graphs.graph_node import GraphNode


class Testgraph_node(TestCase):

    graph = None
    test_node = None
    test_node_2 = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.graph = Graph()
        cls.test_node = GraphNode("first")
        cls.graph.sub_graphs.append(cls.test_node)
        cls.test_node_2 = GraphNode("second")
        cls.graph.sub_graphs[0].add_node(cls.test_node_2)

    def test_value(self):
        self.assertEqual(self.graph.sub_graphs[0].value, "first")

    def test_add_node(self):

        self.assertEqual(self.graph.sub_graphs[0].adjacent_nodes[0], self.test_node_2)

    def test_adjacent_nodes(self):
        self.assertTrue(self.test_node_2 in self.graph.sub_graphs[0].adjacent_nodes)

    #def test_is_connected_to_node(self):
    #    self.fail()
