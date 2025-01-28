from collections import deque, defaultdict

class Graph:
    """
    This class represents a graph using an adjacency list.
    The adjacency list is implemented as a dictionary where:
        - Each key is a vertex
        - The value is a list of neighbors
    """
    
    def __init__(self, num_vertices):
        """
        Initializes the graph with the specified number of vertices.
        :param num_vertices: The total number of vertices in the graph.
        """
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(list)  # Adjacency list to store the graph

    def add_edge(self, u, v, directed=True):
        """
        Adds an edge between vertices u and v.
        If directed is False, it adds the edge in both directions.
        
        :param u: The starting vertex of the edge.
        :param v: The ending vertex of the edge.
        :param directed: Boolean indicating if the edge is directed (default is True).
        """
        self.adj_list[u].append(v)  # Add directed edge from u to v

        if not directed:
            self.adj_list[v].append(u)  # If undirected, add reverse edge

    def topological_sort_dfs(self):
        """
        Performs topological sorting using DFS.
        """
        visited = set()
        stack = []

        for node in range(self.num_vertices):
            if node not in visited:
                self.dfs_helper(node, visited, stack)
        
        return stack[::-1]
    
    def dfs_helper(self, node, visited, stack):
        """
        Helper function for the DFS-based topological sort.
        """
        visited.add(node)
        for neighbor in self.adj_list.get(node, []):
            if neighbor not in visited:
                self.dfs_helper(neighbor, visited, stack)
        stack.append(node)

    def topological_sort_bfs(self):
        """
        Performs topological sorting using BFS (Kahn's Algorithm).
        """
        indegree = [0] * self.num_vertices
        
        # Calculate indegree for each vertex
        for node in range(self.num_vertices):  # Iterate over all vertices
            for neighbor in self.adj_list[node]:
                indegree[neighbor] += 1

        # Initialize the queue with vertices having indegree 0
        queue = deque()
        for i in range(self.num_vertices):
            if indegree[i] == 0:
                queue.append(i)        
        
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If all nodes are not processed, it means there is a cycle
        if len(result) != self.num_vertices:
            return -1

        return result


# Example usage:
if __name__ == "__main__":
    # Create a graph with 5 vertices
    graph = Graph(5)
    
    # Add edges to the graph (directed)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 4)

    # Print the adjacency list representation of the graph
    print("Adjacency List Representation:")
    for vertex, edges in graph.adj_list.items():
        print(f"{vertex}: {edges}")

    # Perform topological sort using DFS
    topological_sort_dfs = graph.topological_sort_dfs()
    print("\nTopological Sort (DFS):")
    print(topological_sort_dfs)

    # Perform topological sort using BFS
    topological_sort_bfs = graph.topological_sort_bfs()
    print("\nTopological Sort (BFS):")
    print(topological_sort_bfs)
