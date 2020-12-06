class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kthLargest(root: TreeNode, k: int) -> int:
    res = []
    def dfs(node: TreeNode):
        if node is None: return
        dfs(node.right)
        if len(res) >= k:
            return
        res.append(node.val)
        dfs(node.left)
    dfs(root)
    return res
