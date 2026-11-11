from collections import deque

print("=== ASSESSMENT 3.4: BINARY TREE TRAVERSAL ===")
print("Last Name Reference: SABANDO\n")


# Node structure para sa Binary Tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Paghimo sa Tree structure base sa SABANDO
#         S (Root)
#       /   \
#      A     B
#     / \     \
#    N   D     O

root = TreeNode('S')
root.left = TreeNode('A')
root.right = TreeNode('B')
root.left.left = TreeNode('N')
root.left.right = TreeNode('D')
root.right.right = TreeNode('O')


# 1. Breadth-First Search (BFS / Level Order Traversal)
def bfs_binary_tree(root):
    if not root:
        return
    queue = deque([root])
    visited = []

    while queue:
        current = queue.popleft()
        visited.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    print("Binary Tree BFS (Level-Order):", " -> ".join(visited))


# 2. Depth-First Search (DFS / Pre-order Traversal)
def dfs_binary_tree(node, visited=None):
    if visited is None:
        visited = []
    if node:
        visited.append(node.val)
        dfs_binary_tree(node.left, visited)
        dfs_binary_tree(node.right, visited)
    return visited


# Pagtawag sa mga functions
bfs_binary_tree(root)
dfs_result = dfs_binary_tree(root)
print("Binary Tree DFS (Pre-Order):", " -> ".join(dfs_result))