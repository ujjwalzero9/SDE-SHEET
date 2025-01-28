class AdjacencyMatrixGraph:
    """
    This class represents a graph using an adjacency matrix.
    The matrix is a 2D list where each cell (i, j) stores the weight of the edge from vertex i to vertex j.
    """
    
    def __init__(self, num_vertices):
        """
        Initializes a graph with the specified number of vertices.
        :param num_vertices: Total number of vertices in the graph
        """
        # Create a square matrix initialized to 0 (no edges between any vertices)
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1, directed=False):
        """
        Adds an edge between vertices u and v with a specified weight.
        If the graph is undirected, the edge is added in both directions.
        :param u: Starting vertex of the edge
        :param v: Ending vertex of the edge
        :param weight: Weight of the edge (default is 1)
        :param directed: Boolean indicating whether the edge is directed (default is False)
        """
        # Add an edge from u to v
        self.matrix[u][v] = weight
        
        # If the graph is undirected, add an edge from v to u as well
        if not directed:
            self.matrix[v][u] = weight


class AdjacencyListGraph:
    """
    This class represents a graph using an adjacency list.
    The adjacency list is a dictionary where each key is a vertex, and the value is a list of tuples
    (neighbor, edge_weight) representing the edges connected to that vertex.
    """

    def __init__(self, num_vertices):
        """
        Initializes a graph with the specified number of vertices.
        :param num_vertices: Total number of vertices in the graph
        """
        # Initialize the adjacency list as an empty dictionary
        self.adj_list = {}

    def add_edge(self, u, v, weight=1, directed=False):
        """
        Adds an edge between vertices u and v with a specified weight.
        If the graph is undirected, the edge is added in both directions.
        :param u: Starting vertex of the edge
        :param v: Ending vertex of the edge
        :param weight: Weight of the edge (default is 1)
        :param directed: Boolean indicating whether the edge is directed (default is False)
        """
        # Add the edge from u to v in the adjacency list
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append((v, weight))

        # If the graph is undirected, add the reverse edge from v to u
        if not directed:
            if v not in self.adj_list:
                self.adj_list[v] = []
            self.adj_list[v].append((u, weight))


if __name__ == "__main__":
    # Create a graph using an adjacency matrix representation
    graph1 = AdjacencyMatrixGraph(5)
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 2)
    graph1.add_edge(0, 3)
    graph1.add_edge(1, 4)
    graph1.add_edge(2, 3)
    graph1.add_edge(3, 4)

    # Print the adjacency matrix
    print("Adjacency Matrix Representation:")
    for row in graph1.matrix:
        print(row)

    # Create a graph using an adjacency list representation
    graph2 = AdjacencyListGraph(5)
    graph2.add_edge(0, 1)
    graph2.add_edge(0, 2)
    graph2.add_edge(0, 3)
    graph2.add_edge(1, 4)
    graph2.add_edge(2, 3)
    graph2.add_edge(3, 4)

    # Print the adjacency list
    print("------------------------------------------")
    print("Adjacency List Representation:")
    for vertex, edges in graph2.adj_list.items():
        print(f"{vertex}: {edges}")
