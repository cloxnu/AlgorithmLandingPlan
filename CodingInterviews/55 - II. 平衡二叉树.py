class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root: TreeNode) -> bool:
    def depth(node: TreeNode):
        if node is None: return 0
        return max(depth(node.left), depth(node.right)) + 1
    if root is None: return True
    return -1 <= depth(root.left) - depth(root.right) <= 1 and isBalanced(root.left) and isBalanced(root.right)

