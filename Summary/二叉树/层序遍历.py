class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def visit(self):
        print(self.value, end=" ") # 访问当前结点


# =================
# 迭代形式（队列）
# =================

def levelorder_iter(root: TreeNode):
    if root is None: return
    queue = [root]
    while queue:
        node = queue.pop(0)
        node.visit()
        if node.left is not None: queue.append(node.left)
        if node.right is not None: queue.append(node.right)


# =================
# 递归形式
# =================

def levelorder(root: TreeNode):
    if root is None: return




# ### 测试树
# 
#        A
#      /   \
#     B     C
#    / \   / \
#   D   E F   G
#        / \
#       H   I
#
#
# 正确的前序遍历： A B D E C F H I G
# 正确的中序遍历： D B E A H F I C G
# 正确的后序遍历： D E B H I F G C A
# 正确的层序遍历： A B C D E F G H I
#
# ###

test = TreeNode('A', left=TreeNode('B', left=TreeNode('D'), right=TreeNode('E')), right=TreeNode('C', left=TreeNode('F', left=TreeNode('H'), right=TreeNode('I')), right=TreeNode('G')))
levelorder(test)

