# 🚀 Time & Space Complexity:
# Time: O(n) – where n is the number of nodes in the tree.
# Space: O(d) – where d is the depth of the tree (for recursion stack).

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def solve(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value  # fixed here

    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)

# Helper function to build tree with shorthand
def buildTree():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    return root

# Test
root = buildTree()
print(solve(root))  # Output: [7, 8, 10, 11]
