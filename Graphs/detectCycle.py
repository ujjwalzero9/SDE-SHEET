class Graph:
    """
    This class represents a graph using an adjacency list.
    The adjacency list is implemented as a dictionary where:
        - Each key is a vertex
        - The value is a list of tuples representing the neighbors and the edge weight
    """
    
    def __init__(self, num_vertices):
        """
        Initializes the graph with the specified number of vertices.
        :param num_vertices: The total number of vertices in the graph.
        This constructor initializes an empty adjacency list.
        """
        self.adj_list = {}  # Adjacency list to store the graph
        self.num_vertices = num_vertices  # Total number of vertices

    def add_edge(self, u, v, weight=1, directed=False):
        """
        Adds an edge between vertices u and v with a specified weight.
        If the graph is undirected, the edge is added in both directions.
        
        :param u: The starting vertex of the edge.
        :param v: The ending vertex of the edge.
        :param weight: The weight of the edge (default is 1).
        :param directed: Boolean indicating if the edge is directed (default is False).
        """
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append((v, weight))

        if not directed:
            if v not in self.adj_list:
                self.adj_list[v] = []
            self.adj_list[v].append((u, weight))

    def detect_cycle_undirected(self):
        """
        Detects if there is a cycle in the undirected graph.
        :return: True if there is a cycle, otherwise False
        """
        visited = [False] * self.num_vertices  # Initialize a list of booleans to track visited nodes
        for node in range(self.num_vertices):
            if not visited[node]:  # If the node hasn't been visited
                if self.dfs_helper_undirected(node, visited, -1):  # Start DFS from this node
                    return True  # If a cycle is detected, return True
        return False  # No cycle detected

    def dfs_helper_undirected(self, node, visited, parent):
        """
        Helper function for DFS to detect cycles.
        :param node: The current node being visited
        :param visited: List to track visited nodes
        :param parent: The parent node of the current node
        :return: True if a cycle is detected, otherwise False
        """
        visited[node] = True  # Mark the current node as visited

        # Explore all neighbors of the current node
        for neighbour, _ in self.adj_list.get(node, []):
            if not visited[neighbour]:  # If the neighbor hasn't been visited
                if self.dfs_helper_undirected(neighbour, visited, node):  # Recurse
                    return True  # If a cycle is detected, return True
            elif neighbour != parent:  # If the neighbor is visited and not the parent, a cycle is detected
                return True

        return False  # No cycle detected from this node


    def detect_cycle_directed(self):
        """
        Detects if there is a cycle in the directed graph.
        :return: True if there is a cycle, otherwise False
        """
        visited = [False] * self.num_vertices  # Initialize a list of booleans to track visited nodes
        rescursion_stack = [False] * self.num_vertices  # Stack to track nodes in the current recursion path
        
        for node in range(self.num_vertices):
            if not visited[node]:  # If the node hasn't been visited
                if self.dfs_helper_directed(node, visited, rescursion_stack):  # Start DFS from this node
                    return True  # If a cycle is detected, return True
        return False  # No cycle detected

    def dfs_helper_directed(self, node, visited, rescursion_stack):
        """
        Helper function for DFS to detect cycles in a directed graph.
        :param node: The current node being visited
        :param visited: List to track visited nodes
        :param rescursion_stack: List to track nodes in the current recursion stack
        :return: True if a cycle is detected, otherwise False
        """
        visited[node] = True  # Mark the current node as visited
        rescursion_stack[node] = True  # Mark the current node as part of the recursion stack

        # Explore all neighbors of the current node
        for neighbour, _ in self.adj_list.get(node, []):
            if rescursion_stack[neighbour]:  # If the neighbor is already in the recursion stack, a cycle exists
                return True
            if not visited[neighbour]:  # If the neighbor hasn't been visited yet
                if self.dfs_helper_directed(neighbour, visited, rescursion_stack):  # Recurse
                    return True  # If a cycle is detected, return True

        rescursion_stack[node] = False  # Unmark the node from the recursion stack once all neighbors are processed
        return False  # No cycle detected from this node

if __name__ == "__main__":
    # Create a graph
    graph1 = Graph(5)
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 2)
    graph1.add_edge(0, 3)
    graph1.add_edge(1, 4)
    graph1.add_edge(2, 3)
    # Uncomment the following line to create a cycle
    #graph1.add_edge(3, 4)

    has_cycle = graph1.detect_cycle_undirected()
    print("Cycle detected:", has_cycle)


# Create another graph with enough vertices
    graph2 = Graph(4)  # Initialize the graph with 4 vertices (0, 1, 2, 3)
    graph2.add_edge(0, 1, directed=True)
    graph2.add_edge(1, 2, directed=True)
    graph2.add_edge(2, 3, directed=True)
    # Uncomment the following line to create a cycle
    #graph2.add_edge(3, 1, directed=True)
    
    has_cycle2 = graph2.detect_cycle_directed()
    print("Cycle detected:", has_cycle2)