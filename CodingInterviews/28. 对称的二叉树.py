class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root: TreeNode) -> bool:
    def isEqual(left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and isEqual(left.left, right.right) and isEqual(left.right, right.left)

    if root is None: return True
    return isEqual(root.left, root.right)
