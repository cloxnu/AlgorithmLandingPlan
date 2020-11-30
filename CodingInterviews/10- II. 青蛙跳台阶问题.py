# 递归
def numWays_rec(n: int) -> int:
    return numWays_rec(n - 1) + numWays_rec(n - 2) if n >= 2 else 1

# 动态规划 O(1) 空间
def numWays(n: int) -> int:
    if n < 2:
        return 1
    prepre = 1
    pre = 1
    curr = 2
    for _ in range(2, n+1):
        curr = prepre + pre
        prepre = pre
        pre = curr
    return curr

print(numWays(10))
