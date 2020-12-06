class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> list:
    res = []
    queue = [root]
    while queue:
        levelres = []
        levelnode = []
        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            levelres.append(node.val)
            levelnode.append(node)
        if not levelres:
            continue
        res.append(levelres)
        for node in levelnode:
            queue.append(node.left)
            queue.append(node.right)
    return res
