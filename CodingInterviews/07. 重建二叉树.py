# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        
        def recur(node: TreeNode, pre: list[int], ino: list[int]):
            if node is None: return
            idx = ino.index(pre[0])
            if idx >= 1:
                node.left = TreeNode(pre[1])
                recur(node.left, pre[1:idx+1], ino[:idx])
            if len(pre) - idx - 1 >= 1:
                node.right = TreeNode(pre[idx+1])
                recur(node.right, pre[idx+1:], ino[idx+1:])

        if len(preorder) == 0: return None
        root = TreeNode(preorder[0])
        recur(root, preorder, inorder)
        return root
    
