class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> list:
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            continue
        res.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    return res

