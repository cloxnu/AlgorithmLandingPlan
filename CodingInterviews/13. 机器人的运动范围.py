
def movingCount(m: int, n: int, k: int) -> int:
    def digitsum(x: int) -> int:
        res = 0
        while x != 0:
            res += x % 10
            x //= 10
        return res

    queue = [(0, 0)]
    res = 0
    visit = {}
    while queue:
        x, y = queue.pop(0)
        if x >= m or y >= n or x < 0 or y < 0:
            continue
        if (x, y) in visit:
            continue
        if digitsum(x) + digitsum(y) > k:
            continue
        visit[(x, y)] = True
        res += 1
        queue.append((x + 1, y))
        queue.append((x - 1, y))
        queue.append((x, y + 1))
        queue.append((x, y - 1))
    return res


print(movingCount(2, 3, 1))
