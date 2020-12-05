class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSubStructure(A: TreeNode, B: TreeNode) -> bool:
    if B is None or A is None: return False
    def isEqual(A: TreeNode, B: TreeNode) -> bool:
        if B is None: return True
        if A is None or B is None: return False
        return A.val == B.val and isEqual(A.left, B.left) and isEqual(A.right, B.right)
    def isSub(A: TreeNode, B: TreeNode) -> bool:
        if A is None: return False
        return isEqual(A, B) or isSub(A.left, B) or isSub(A.right, B)
    return isSub(A, B)
