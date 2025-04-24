# Depth-First Search (DFS)

# V = number of vertices (nodes) in the graph
# E = number of edges
# 🔍 Time Complexity: O(V + E)
# 🧠 Space Complexity: O(V)

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        child = Node(name)
        self.children.append(child)
        return self  # allows chaining

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


# Constructing the graph manually using Node objects
# Graph structure:
#       A
#     /   \
#    B     C
#   / \     \
#  D   E     F

a = Node("A")
a.addChild("B").addChild("C")
a.children[0].addChild("D").addChild("E")  # B -> D, E
a.children[1].addChild("F")               # C -> F

# DFS traversal starting from node A
print(a.depthFirstSearch([]))  # Output: ['A', 'B', 'D', 'E', 'C', 'F']

# OUTPUT
#--------
# ['A', 'B', 'D', 'E', 'C', 'F']