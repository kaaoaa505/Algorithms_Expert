# Breadth-First Search (BFS)
# Iterative BFS Node Depth Calculation

# Time Complexity: 𝑂(𝑛) 
# Space Complexity: 𝑂(𝑛) 

# 𝑛 = total number of nodes in the tree.

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def solve(root):
    queue = deque()
    queue.append((root, 0))

    while queue:
        node, depth = queue.popleft()
        print(f"Node {node.value} has depth {depth}")
        for child in node.children:
            queue.append((child, depth + 1))

# Create nodes
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

# Build the tree
A.children = [B, C]
B.children = [D]
C.children = [E, F]

# Run the BFS version
solve(A)
