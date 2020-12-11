class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is None or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if not left:
        return right
    elif not right:
        return left
    else:
        return root


def lowestCommonAncestor2(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

    def findNode(node: TreeNode, search: TreeNode) -> (list, bool):
        if node is None:
            return [], False
        if node == search:
            return [search], True

        left, leftFind = findNode(node.left, search)
        if leftFind:
            return left + [node], leftFind

        right, rightFind = findNode(node.right, search)
        if rightFind:
            return right + [node], rightFind

        return [], False

    pathP, isFindP = findNode(root, p)
    pathQ, isFindQ = findNode(root, q)

    if not isFindP or not isFindQ:
        return None

    pathP.reverse()
    pathQ.reverse()
    last, p_ptr, q_ptr = 0, 0, 0

    while p_ptr < len(pathP) and q_ptr < len(pathQ):
        if pathP[p_ptr] == pathQ[q_ptr]:
            last = pathP[p_ptr]
            p_ptr += 1
            q_ptr += 1
        else: break
    return last

E = TreeNode('E')
F = TreeNode('F', left=TreeNode('H'), right=TreeNode('I'))
test = TreeNode('A', left=TreeNode('B', left=TreeNode('D'), right=E),
                right=TreeNode('C', left=F,
                right=TreeNode('G')))

print(lowestCommonAncestor2(test, E, F))



