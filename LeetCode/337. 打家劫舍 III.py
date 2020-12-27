class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0, 0
            lr, lnr = dfs(node.left)
            rr, rnr = dfs(node.right)
            r = lnr + rnr + node.val
            nr = max(lr, lnr) + max(rr, rnr)
            return r, nr
        r, nr = dfs(root)
        return max(r, nr)
