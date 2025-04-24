# Depth-First Search (DFS)
# traversal implemented recursively.

# V = number of vertices (nodes) in the graph
# E = number of edges
# 🔍 Time Complexity: O(V + E)
# 🧠 Space Complexity: O(V)

def solve(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            solve(graph, neighbor, visited)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS traversal:")
solve(graph, 'A')

# OUTPUT
#--------
# DFS traversal:
# A B D E C F
