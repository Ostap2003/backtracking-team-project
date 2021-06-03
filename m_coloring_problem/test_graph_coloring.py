"""
A module with unittests for testing graph coloring.
"""
import unittest
from graph_coloring import Graph
from unittest import TestCase


class TestGraphColoring(TestCase):

    def setUp(self):
        pass

    def test_nonexistent_coloring(self):
        """ Try to solve graph coloring problem without the sufficient number of colors """
        adj_matrix = [[0, 1, 1, 1],
                      [1, 0, 1, 0],
                      [1, 1, 0, 1],
                      [1, 0, 1, 0]]
        graph = Graph(adj_matrix)

        self.assertEqual(graph.get_graph_coloring(1), False)
        self.assertEqual(graph.get_graph_coloring(2), False)

    def test_sufficient_coloring(self):
        """ Check proposed m-coloring solution"""
        adj_matrix = [[0, 1, 1, 1],
                      [1, 0, 1, 0],
                      [1, 1, 0, 1],
                      [1, 0, 1, 0]]
        graph = Graph(adj_matrix)
        self.assertEqual(bool(graph.get_graph_coloring(5)), True)

        proposed_solution = graph.get_graph_coloring(5)
        vertex_color_safety = []  # store bool values of validity of the given color assignments
        for vertex_id, proposed_vertex_color in enumerate(proposed_solution):
            for adj_vertex_id, adj_vertex in enumerate(adj_matrix[vertex_id]):
                if adj_vertex == 1 and proposed_solution[adj_vertex_id] == proposed_vertex_color:
                    # Append False to the list because current color assignment is unsafe
                    vertex_color_safety.append(False)
                else:
                    vertex_color_safety.append(True)

        self.assertEqual(all(vertex_color_safety), True)


if __name__ == '__main__':
    unittest.main()
