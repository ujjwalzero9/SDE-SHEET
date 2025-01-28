import heapq

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

    def dijkstra(self, start):
        """
        Implements Dijkstra's algorithm to find the shortest path from the start vertex.
        :param start: The starting vertex.
        :return: A list with the shortest distance from the start vertex to each other vertex.
        
        Time Complexity:
        - O((V + E) * log(V)), where V is the number of vertices and E is the number of edges.
        This is because each edge is processed once and heap operations (push and pop) take log(V) time.
        """
        # Initialize distances as a list of infinity values
        distances = [float('inf')] * self.num_vertices
        distances[start] = 0

        # Priority queue to explore the graph, starting from the start node
        pq = [(0, start)]  # (distance, vertex)

        while pq:
            # Get the vertex with the smallest distance
            current_distance, current_vertex = heapq.heappop(pq)

            # If we already found a shorter path to current_vertex, skip it
            if current_distance > distances[current_vertex]:
                continue

            # Explore the neighbors of the current vertex
            for neighbor, weight in self.adj_list.get(current_vertex, []):
                distance = current_distance + weight

                # If a shorter path to the neighbor is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances
    
    def bellman_ford(self, start):
        """
        Implements Bellman-Ford algorithm to find the shortest path from the start vertex.
        :param start: The starting vertex.
        :return: A list with the shortest distance from the start vertex to each other vertex.
        
        Time Complexity:
        - O(V * E), where V is the number of vertices and E is the number of edges.
        This is because we need to relax all edges V-1 times, and each relaxation operation takes O(E) time.
        """
        # Initialize distances as a list of infinity values
        distances = [float('inf')] * self.num_vertices
        distances[start] = 0
        
        # Relax all edges V-1 times
        for _ in range(self.num_vertices - 1):
            # Check each edge
            for u in self.adj_list:
                for v, weight in self.adj_list[u]:
                    if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
        
        # Check for negative weight cycles
        for u in self.adj_list:
            for v, weight in self.adj_list[u]:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    print("Graph contains a negative weight cycle")
                    return None
        
        return distances


# Driver Code
if __name__ == "__main__":
    # Create a graph with 5 vertices (0 to 4)
    graph = Graph(5)

    # Add edges to the graph
    graph.add_edge(0, 1, weight=10)
    graph.add_edge(0, 2, weight=5)
    graph.add_edge(1, 2, weight=2)
    graph.add_edge(1, 3, weight=1)
    graph.add_edge(2, 3, weight=9)
    graph.add_edge(3, 4, weight=4)

    # Print the adjacency list of the graph
    print("Adjacency List:")
    for vertex, edges in graph.adj_list.items():
        print(f"{vertex}: {edges}")

    # Run Dijkstra's algorithm from vertex 0
    distances = graph.dijkstra(0)

    # Output the shortest distances from vertex 0 to all other vertices
    print("\nShortest distances from vertex 0:")
    for vertex, distance in enumerate(distances):
        print(f"Distance from 0 to {vertex}: {distance}")


    distances2 = graph.bellman_ford(0)

    # Output the shortest distances from vertex 0 to all other vertices
    print("\nBellman Ford Shortest distances from vertex 0:")
    for vertex, distance in enumerate(distances2):
        print(f"Distance from 0 to {vertex}: {distance}")
