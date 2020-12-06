class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root: TreeNode) -> int:
    def dfs(node: TreeNode, depth):
        if node is None:
            return depth
        return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
    return dfs(root, 0)
