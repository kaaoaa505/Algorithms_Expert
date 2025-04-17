# 🚀 Time & Space Complexity:
# Time: O(n) – where n is the number of nodes in the tree.

# Space: O(d) – where d is the depth of the tree (for recursion stack).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.val  # fixed from node.value

    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)

# Example tree:
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7

root = TreeNode(1) 
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))

print(solve(root))  # Output: [7, 8, 10, 11]
