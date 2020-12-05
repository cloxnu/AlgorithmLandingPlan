class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mirrorTree(self, root: TreeNode) -> TreeNode:
    def mirror(node: TreeNode):
        if node is None: return
        node.left, node.right = node.right, node.left
        mirror(node.left)
        mirror(node.right)
    mirror(root)
    return root
