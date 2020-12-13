import copy


# 递归实现：仅使用 start end 和 交换
def permutation(ls: list) -> list:
    res = []

    def recur(start, end):
        if start >= end:
            res.append(ls[:])
            return
        for idx in range(start, end):
            ls[start], ls[idx] = ls[idx], ls[start]  # 将选择过的 item 交换到前面
            recur(start + 1, end)  # 下一次迭代就不包含上一次选择过的 item
            ls[start], ls[idx] = ls[idx], ls[start]

    recur(0, len(ls))
    return res


# 递归实现 2：将 list 传递
def permutation2(ls: list) -> list:
    res = []

    def recur(l: list, reduce: list):
        if len(l) == 0:
            res.append(reduce)
            return
        for idx in range(len(l)):
            new = copy.copy(l)  # 拷贝新 list
            del new[idx]
            recur(new, reduce + [l[idx]])

    recur(ls, [])
    return res


# 迭代实现：将 list 存入栈 / 队列
def permutation_iter(ls: list) -> list:
    res = []
    stack = [(ls, [])]
    while stack:
        l, reduce = stack.pop()  # 队列也可
        if len(l) == 0:
            res.append(reduce)
            continue
        for idx in reversed(range(len(l))):  # 不 reverse 也可
            new = copy.copy(l)
            del new[idx]
            stack.append((new, reduce + [l[idx]]))
    return res


print(permutation_iter([2, 3, 4]))
