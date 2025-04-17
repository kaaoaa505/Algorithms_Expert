# 🔧 Problem Definition:
- Given a binary tree, 
- return a list of the sums of all branches. 
- A branch is a path of nodes from the root node down to a leaf node.

# ✅ Example:
Given this binary tree:

                      1
                    /   \
                   2     3
                  / \   / \
                 4   5 6   7

# Branch sums are:

1 + 2 + 4 = 7

1 + 2 + 5 = 8

1 + 3 + 6 = 10

1 + 3 + 7 = 11

➡️ Output: [7, 8, 10, 11]



# 🧠 Approach (Recursive):
1- Start at the root.

2- Recursively go down each path, accumulating the sum.

3- When you reach a leaf, add the current path sum to the result list.