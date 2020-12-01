# 重中之重！！

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def visit(self):
        print(self.value) # 访问当前结点

# 递归形式

## 前序遍历
def preorder(node: TreeNode):
    if node is None: return
    node.visit() # 访问当前结点
    node.preorder(node.left)
    node.preorder(node.right)

## 中序遍历
def inorder(node: TreeNode):
    if node is None: return
    node.inorder(node.left)
    node.visit() # 访问当前结点
    node.inorder(node.right)

## 后序遍历
def postorder(node: TreeNode):
    if node is None: return
    node.postorder(node.left)
    node.postorder(node.right)
    node.visit() # 访问当前结点


# 迭代形式

## 前序遍历 1：栈模拟
def preorder_iter(root: TreeNode):
    if root is None: return
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None: continue
        node.visit() # 访问当前结点
        stack.append(node.right) # 先入栈右子树
        stack.append(node.left) # 再入栈左子树

## 中序遍历
def inorder_iter(root: TreeNode):
    if root is None: return
    stack = []
    node = root
    while node or stack:
        while node: # 先找最左的 node，路途依次入栈
            stack.append(node)
            node = node.left
        node = stack.pop()
        node.visit() # 访问当前结点
        node = node.right

## 后序遍历 1：类前序遍历 1 + reverse：利用双栈将 根-右-左 的结果反过来
def postorder_iter(root: TreeNode):
    if root is None: return
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        if node is None: continue
        res.append(node)
        stack.append(node.left) # 先入栈左子树
        stack.append(node.right) # 再入栈右子树
    for node in reversed(res):
        node.visit()

