
# 遇到后序遍历，先想到把后序反过来，就变成了 根-右-左

# [1, 3, 2, 6, 5]
# [1, 6, 3, 2, 5]

# 递归解法
def verifyPostorder(postorder: list) -> bool:
    def recur(left, right):
        if left >= right - 1: return True
        for i in range(left, right):
            if postorder[i] > postorder[right]:
                for j in range(i, right):
                    if postorder[j] < postorder[right]:
                        return False
                return recur(left, i-1) and recur(i, right-1)
        return recur(left, right - 1)

    return recur(0, len(postorder)-1)


# 单调栈解法
def verifyPostorder2(postorder: list) -> bool:
    stack, root = [], None
    for i in reversed(postorder):
        if root is not None and i > root:
            return False
        while stack and stack[-1] > i:
            root = stack.pop()
        stack.append(i)
    return True


print(verifyPostorder2([]))
