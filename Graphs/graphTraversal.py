from collections import deque

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

    def add_edge(self, u, v, weight=1, directed=False):
        """
        Adds an edge between vertices u and v with a specified weight.
        If the graph is undirected, the edge is added in both directions.
        
        :param u: The starting vertex of the edge.
        :param v: The ending vertex of the edge.
        :param weight: The weight of the edge (default is 1).
        :param directed: Boolean indicating if the edge is directed (default is False).
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

    def bfs(self, start_node):
        """
        Performs a Breadth-First Search (BFS) traversal starting from the given node.
        BFS explores all neighbors of the current node before moving to the next level neighbors.
        
        :param start_node: The node from which BFS traversal starts.
        :return: A list of nodes in the order they were visited during BFS.
        """
        visited = set()  # Set to keep track of visited nodes
        traversal = []  # List to store the order of traversal
        queue = deque([start_node])  # Queue for BFS initialization with the start node

        while queue:
            node = queue.popleft()  # Pop the first node from the queue
            if node not in visited:
                traversal.append(node)  # Add the node to the traversal list
                visited.add(node)  # Mark the node as visited

            # Explore the neighbors of the current node
            for neighbor, weight in self.adj_list.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)  # Add unvisited neighbors to the queue

        return traversal  # Return the order of traversal

    def dfs(self, node, visited=None, traversal=None):
        """
        Performs a Depth-First Search (DFS) traversal starting from the given node.
        DFS explores as far as possible along a branch before backtracking.
        
        :param node: The current node to explore.
        :param visited: Set of visited nodes (default is None).
        :param traversal: List of nodes visited during DFS (default is None).
        :return: A list of nodes in the order they were visited during DFS.
        """
        # Initialize visited and traversal if not already done
        if visited is None:
            visited = set()
        if traversal is None:
            traversal = []

        traversal.append(node)  # Add the current node to the traversal list
        visited.add(node)  # Mark the current node as visited

        # Explore the neighbors of the current node
        for neighbor, weight in self.adj_list.get(node, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited, traversal)  # Recursively visit unvisited neighbors

        return traversal  # Return the order of traversal

# Example usage:
if __name__ == "__main__":
    # Create a graph with 5 vertices
    graph = Graph(5)
    
    # Add edges to the graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    # Print the adjacency list representation of the graph
    print("Adjacency List Representation:")
    for vertex, edges in graph.adj_list.items():
        print(f"{vertex}: {edges}")

    # Perform BFS traversal starting from node 0
    bfs_result = graph.bfs(0)
    print("BFS Traversal:", bfs_result)

    # Perform DFS traversal starting from node 0
    dfs_result = graph.dfs(0)
    print("DFS Traversal:", dfs_result)
