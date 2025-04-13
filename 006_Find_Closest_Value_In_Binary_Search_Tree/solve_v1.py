# ⏱️ Time Complexity: O(h)
# At each step, you move either left or right, never both.
# So you traverse at most h nodes, 
# where h is the height of the tree.
# In the best case (balanced BST):
# h = log(n) → O(log n)
# In the worst case (unbalanced/skewed BST):
# h = n → O(n)
# ✅ So, time complexity = O(h)

# 💾 Space Complexity: O(1) (iterative version)
# You only use a few variables to keep track 
# (closest, current) — no recursion stack.
# So this is constant space.
# ✅ So, space complexity = O(1)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, target: float) -> int:
    closest = root.val
    current = root

    while current:
        # Update closest if the current node is closer to target
        if abs(target - current.val) < abs(target - closest):
            closest = current.val

        # Move left or right based on target
        if target < current.val:
            current = current.left
        elif target > current.val:
            current = current.right
        else:
            break  # Exact match found

    return closest

# BST Example:
#       4
#      / \
#     2   5
#    / \
#   1   3

root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(5)

target = 3.714286
print(solve(root, target))  # Output: 4

target = 2
print(solve(root, target))  # Output: 2

target = 2.6
print(solve(root, target))  # Output: 3
