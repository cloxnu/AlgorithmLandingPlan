def validateStackSequences(self, pushed: list, popped: list) -> bool:
    if not pushed: return True
    visit = [False for _ in range(len(pushed))]

    for pop_val in popped:
        idx = pushed.index(pop_val)
        visit[idx] = True
        for j in range(idx, len(pushed)):
            falseFlag = False
            if not visit[j]:
                falseFlag = True
            if falseFlag and visit[j]:
                return False

    return True


# 时间复杂度太高了
