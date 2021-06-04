"""
A module with the Graph class for solving graph coloring problem.
"""


class Graph:

    def __init__(self, adj_matrix):
        """
        :param adj_matrix: Adjacency matrix of a graph
        """
        self.adj_matrix = adj_matrix
        self.coloring = [None for vertex in range(len(self.adj_matrix))]

    def check_color_safety(self, adj_vertices, color):
        """
        Check for color safety for the current vertex.
        If all adjacent vertices do not share this certain color, then it is safe.

        :param adj_vertices: adjacency list for the certain vertex
        :param color: color to be tested for current vertex safety
        :return: True if color is safe, else False
        """
        for adj_vertex_id, adj_vertex in enumerate(adj_vertices):
            if adj_vertex == 1 and self.coloring[adj_vertex_id] == color:
                return False
        return True

    def get_graph_coloring(self, num_colors):
        """
        Determine whether the graph could be colored with {num_colors} colors.
        No two adjacent vertices of the graph should have the same color.

        :param num_colors: Number of possible colors given to color this graph.
        :return: color assignment in form of a list, with the numbers in from 1 to {num_colors},
            where [i] index represents the color assigned to ith vertex. If it doesn't exist return False
        """
        self.coloring = [None for vertex in
                         range(len(self.adj_matrix))]  # reset graph coloring if it was previously used

        for vertex_id, adj_vertices in enumerate(self.adj_matrix):
            for color in range(1, num_colors + 1):
                if self.check_color_safety(adj_vertices, color):
                    self.coloring[vertex_id] = color
                    break

        if not all(self.coloring):  # return False if some vertices do not have a color assigned
            print(f"Coloring current graph with {num_colors} colors is impossible")
            return False

        print(f"Solution for coloring current graph with {num_colors} colors:\n{self.coloring}")
        return self.coloring
