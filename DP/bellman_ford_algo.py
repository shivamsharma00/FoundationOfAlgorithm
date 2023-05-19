# weighted directed graph implementation
class graph:
    def init(self, edges, n):
    # Initialize an empty adjacency list for each node
        self.adjacency_list = [None] * n
            # Allocate memory to the adjacency list
        for i in range(n):
            self.adjacency_list[i] = []
    
        # Add edges to the directed graph
        for (src, dest, weight) in edges:
            self.adjacency_list[src].append((dest, weight))
    
# Function to print the adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adjacency_list)):
        for (dest, weight) in graph.adjacency_list[src]:
            print(f'({src} -> {dest}, {weight})', end='')
            print()

if __name__ == '__main__':
    edges = [(1, 2, 9), (1, 3, 6), (1, 5, 15), (2, 4, -5), (2, 3, -2), (3, 5, -8), (4, 3, 1), (4, 6, 1), (5, 4, 10), (5, 6, 3)]

    # Determine the total number of unique nodes in the graph
    nodes = set(edges[i][j] for i in range(len(edges)) for j in range(2))
    total_nodes = len(nodes)  
    total_edges = len(edges)
    
    # Create an instance of the graph class
    graph_ = graph(edges, total_nodes)
    
    # Print the adjacency list representation of the graph
    printGraph(graph_)
    
    # Create a matrix M to store the shortest path distances
    M = [[0 for x in range(total_nodes)] for y in range(total_edges)]
    
    # Initialize the first row of matrix M with a large value
    for x in range(total_nodes):
        M[0][x] = 99999
    
    # Set the destination node distance in the first row to 0
    M[0][total_nodes - 1] = 0
    
    # Calculate the shortest path distances for each edge
    for i in range(1, total_edges):
        for n in nodes:
            M[i][n - 1] = M[i - 1][n - 1]
        
        for node in range(0, total_nodes - 1):
            child = graph_.adjacency_list[node + 1]
    
            for (c, w) in child:
                M[i][node] = min(M[i][node], (M[i - 1][c - 1] + w))
         
    
    # Print the matrix M
    for x in range(total_edges):
        print(M[x])
    