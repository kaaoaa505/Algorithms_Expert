# Recursive Node Depth Calculation

# Time Complexity: 𝑂(𝑛) 
# - 𝑛 = total number of nodes in the tree.
# - each node visited exactly once.

# Space Complexity: 𝑂(ℎ)
# The depth of recursive calls = height of the tree ℎ
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def solve(node, depth=0):
    print(f"Node {node.value} has depth {depth}")
    for child in node.children:
        solve(child, depth + 1)

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

# Run the recursive version
solve(A)