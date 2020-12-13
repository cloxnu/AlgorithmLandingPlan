# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')

        def dfs(node: TreeNode):
            nonlocal res
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            left_val = max((node.left.val if node.left else 0), 0)
            right_val = max((node.right.val if node.right else 0), 0)
            res = max(res, node.val + left_val + right_val)

            node.val += max((left_val if left_val > 0 else 0), (right_val if right_val > 0 else 0))

        dfs(root)
        return res
