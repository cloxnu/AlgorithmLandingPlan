import copy

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def pathSum(root: TreeNode, sum: int) -> list:
    res = []
    onePath = []
    def dfs(s: int, node: TreeNode):
        if node is None: return
        onePath.append(node.val)
        s += node.val
        if node.left is None and node.right is None:
            if s == sum:
                res.append(copy.copy(onePath))
            onePath.pop()
            return
        if node.left:
            dfs(s, node.left)
        if node.right:
            dfs(s, node.right)
        onePath.pop()
    dfs(0, root)
    return res


test = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(5, left=TreeNode(6, left=TreeNode(7), right=TreeNode(8)), right=TreeNode(9)))
print(pathSum(TreeNode(3), 3))

