# 重中之重！！

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def visit(self):
        print(self.value, end=" ")  # 访问当前结点


# =================
# 递归形式
# =================

## 前序遍历
def preorder(node: TreeNode):
    if node is None: return
    node.visit()  # 访问当前结点
    preorder(node.left)
    preorder(node.right)


## 中序遍历
def inorder(node: TreeNode):
    if node is None: return
    inorder(node.left)
    node.visit()  # 访问当前结点
    inorder(node.right)


## 后序遍历
def postorder(node: TreeNode):
    if node is None: return
    postorder(node.left)
    postorder(node.right)
    node.visit()  # 访问当前结点


# =================
# 迭代形式
# =================

## -----------------
## 前/后序栈模拟递归
## -----------------

## 前序遍历 1：栈模拟递归
def preorder_iter(root: TreeNode):
    if root is None: return
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None: continue
        node.visit()  # 访问当前结点
        stack.append(node.right)  # 先入栈右子树
        stack.append(node.left)  # 再入栈左子树


## 后序遍历 1：类前序遍历 1 + reverse：先用栈模拟，再利用双栈将 根-右-左 的结果反过来
def postorder_iter(root: TreeNode):
    if root is None: return
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        if node is None: continue
        res.append(node)
        stack.append(node.left)  # 先入栈左子树
        stack.append(node.right)  # 再入栈右子树
    for node in reversed(res):
        node.visit()


## -----------------
## 树的非递归遍历模板
## -----------------

## 前序遍历 2：树的非递归遍历模板
def preorder_iter2(root: TreeNode):
    if root is None: return
    stack = []
    node = root
    while node or stack:
        while node:  # 先找最左的 node，路途依次入栈
            node.visit()  # 根
            stack.append(node)
            node = node.left  # 左
        node = stack.pop()
        node = node.right  # 右


## 中序遍历：树的非递归遍历模板
def inorder_iter(root: TreeNode):
    if root is None: return
    stack = []
    node = root
    while node or stack:
        while node:  # 先找最左的 node，路途依次入栈
            stack.append(node)
            node = node.left  # 左
        node = stack.pop()
        node.visit()  # 根
        node = node.right  # 右


## 后序遍历 2：类前序遍历 2 + reverse：先用树的非递归模板，再利用双栈将 根-右-左 的结果反过来
def postorder_iter2(root: TreeNode):
    if root is None: return
    stack, res = [], []
    node = root
    while node or stack:
        while node:  # 先找最右的 node，路途依次入栈
            res.append(node)  # 根
            stack.append(node)
            node = node.right  # 右
        node = stack.pop()
        node = node.left  # 左
    for node in reversed(res):
        node.visit()


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

test = TreeNode('A', left=TreeNode('B', left=TreeNode('D'), right=TreeNode('E')),
                right=TreeNode('C', left=TreeNode('F', left=TreeNode('H'), right=TreeNode('I')), right=TreeNode('G')))
postorder_iter2(test)
