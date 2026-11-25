class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder_dfs(node):
    """Pre-order traversal: Root -> Left -> Right"""
    if node is None:
        return []
    return [node.value] + preorder_dfs(node.left) + preorder_dfs(node.right)


def inorder_dfs(node):
    """In-order traversal: Left -> Root -> Right"""
    if node is None:
        return []
    return inorder_dfs(node.left) + [node.value] + inorder_dfs(node.right)


def postorder_dfs(node):
    """Post-order traversal: Left -> Right -> Root"""
    if node is None:
        return []
    return postorder_dfs(node.left) + postorder_dfs(node.right) + [node.value]


def build_tree():
    """I-adjust ang mga node ayon sa tree mo sa Assessment 3.5."""
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    return root


if __name__ == "__main__":
    tree_root = build_tree()
    print("Pre-order  (Root -> Left -> Right):", preorder_dfs(tree_root))
    print("In-order   (Left -> Root -> Right):", inorder_dfs(tree_root))
    print("Post-order (Left -> Right -> Root):", postorder_dfs(tree_root))