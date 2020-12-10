
# 递归实现
def permutation(ls: list) -> list:
    res = []
    def recur(start, end):
        if start >= end:
            res.append(ls[0:end])
            return
        for idx in range(start, end):
            ls[start], ls[idx] = ls[idx], ls[start] # 将选择过的 item 交换到前面
            recur(start + 1, end) # 下一次迭代就不包含上一次选择过的 item
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
        for item in l:



print(permutation([2, 3, 4]))
