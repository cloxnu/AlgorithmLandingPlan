# 「力扣」上的 0-1 背包问题：
#
# 「力扣」第 416 题：分割等和子集（中等）；
# 「力扣」第 474 题：一和零（中等）；
# 「力扣」第 494 题：目标和（中等）；
# 「力扣」第 879 题：盈利计划（困难）；
# 「力扣」上的 完全背包问题：
#
# 「力扣」第 322 题：零钱兑换（中等）；
# 「力扣」第 518 题：零钱兑换 II（中等）；
# 「力扣」第 1449 题：数位成本和为目标值的最大数字（困难）。
# 这里要注意鉴别：「力扣」第 377 题，不是「完全背包」问题。
#

pass

"""
0-1 背包

有 n 个物品，物品有两个属性
代价 cost
价值 value，
背包在容量 space 的限制下可以装物品的最大价值？

假设物品数 n = 3  costs = [1, 2, 5]  values = [3, 7, 15]  space = 7

j       0   1   2   3   4   5   6   7
dp[j]   -----------------------------
init    0   0   0   0   0   0   0   0
1       0   3   3   3   3   3   3   3
1+2     0   3   7   10  10  10  10  10
1+2+3   0   3   7   10  10  15  18  22
"""


def zero_one_back(n: int, costs: list, values: list, space: int):
    dp = [0] * (space + 1)

    for i in range(n):
        for j in reversed(range(space + 1)):
            if j < costs[i]:
                break  # 这里因为 j 是有序的（越来越小），所以可以用 break，否则用 continue
            dp[j] = max(dp[j], dp[j - costs[i]] + values[i])

    return dp[space]


# print(zero_one_back(3, [1, 2, 5], [3, 7, 15], 7))


"""
完全背包

有 n 个物品，物品的数量无限，物品有两个属性
代价 cost
价值 value，
背包在容量 space 的限制下可以装物品的最大价值？

假设物品数 n = 3  costs = [1, 2, 5]  values = [3, 7, 15]  space = 7

j       0   1   2   3   4   5   6   7
dp[j]   -----------------------------
init    0   0   0   0   0   0   0   0
1       0   3   6   9   12  15  18  21
1+2     0   3   7   10  14  17  21  24
1+2+3   0   3   7   10  14  17  21  24
"""


def complete_back(n: int, costs: list, values: list, space: int):
    dp = [0] * (space + 1)

    for i in range(n):
        for j in range(space + 1):
            if j < costs[i]:
                continue  # 这里是 continue
            dp[j] = max(dp[j], dp[j - costs[i]] + values[i])
        print(dp)

    return dp[space]


print(complete_back(3, [1, 2, 5], [3, 7, 15], 7))
