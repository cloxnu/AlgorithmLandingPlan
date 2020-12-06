class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeToDoublyList(root: 'Node') -> 'Node':
    if root is None: return None
    res = []
    def dfs(node: Node):
        if node is None: return
        dfs(node.left)
        res.append(node)
        dfs(node.right)
    dfs(root)
    dummy = curr = Node(0)
    for node in res:
        curr.right = node
        node.left = curr
        curr = node
    dummy.right.left = curr
    curr.right = dummy.right
    return dummy.right

