
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(node: TreeNode, small, big):
            if node is None:
                return True
            # small, big = max(small, root.val), min(big, root.val)
            return (small < node.left.val < node.val if node.left is not None else True) and (big > node.right.val > node.val if node.right is not None else True) and isValid(node.left, small, node.val) and isValid(node.right, node.val, big)
        return isValid(root, float('-inf'), float('inf'))