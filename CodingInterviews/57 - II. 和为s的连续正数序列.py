def findContinuousSequence(target: int) -> list:
    res = []
    for i in reversed(range(2, target // 2 + 2)):
        if i & 1 and target % i == 0:
            center = target // i
            if center - i // 2 <= 0: continue
            l = []
            for j in range(center - i // 2, center + i // 2 + 1):
                l.append(j)
            res.append(l)
        elif i & 1 == 0 and (target / i) % 1 == 0.5:
            center = target // i
            if center - i // 2 + 1 <= 0: continue
            l = []
            for j in range(center - i // 2 + 1, center + i // 2 + 1):
                l.append(j)
            res.append(l)
    return res

print(findContinuousSequence(3))
