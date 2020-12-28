pass

"""
求排列数

爬楼梯 II
一次爬楼梯步数可以为 steps，一共要爬 amount 级台阶，有多少种爬法？

假设 steps = [1, 2, 5]  amount = 7

i       0   1   2   3   4   5   6   7   amount
dp[i]   -----------------------------
init    1   0   0   0   0   0   0   0
1       1   1   0   0   0   0   0   0
2       1   1   2   0   0   0   0   0
3       1   1   2   3   0   0   0   0
4       1   1   2   3   5   0   0   0
5       1   1   2   3   5   9   0   0
6       1   1   2   3   5   9   15  0
7       1   1   2   3   5   9   15  26
"""


def permutation_num(steps: list, amount: int):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for i in range(amount + 1):  # 总量在前
        for step in steps:  # 一次在后
            if i < step:
                continue
            dp[i] += dp[i - step]
        print(dp)

    return dp[amount]


print(permutation_num([1, 2, 5], 7))


"""
求组合数

零钱兑换 II
不同面额的硬币为 steps，总金额为 amount，凑出总金额硬币的组合数

假设 steps = [1, 2, 5]  amount = 7

i       0   1   2   3   4   5   6   7   amount
dp[i]   -----------------------------
init    1   0   0   0   0   0   0   0
1       1   1   1   1   1   1   1   1
2       1   1   2   2   3   3   4   4
3       1   1   2   2   3   4   5   6
"""


def combination_num(steps: list, amount: int):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for step in steps:  # 一次在前
        for i in range(amount + 1):  # 总量在后
            if i < step:
                continue
            dp[i] += dp[i - step]
        print(dp)

    return dp[amount]


print(combination_num([1, 2, 5], 7))
