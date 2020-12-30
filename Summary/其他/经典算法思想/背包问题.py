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

j       0   1   2   3   4   5   6   7   space
dp[j]   -----------------------------
init    0   0   0   0   0   0   0   0
1       0   3   3   3   3   3   3   3
1+2     0   3   7   10  10  10  10  10
1+2+3   0   3   7   10  10  15  18  22
"""


def zero_one_back(n: int, costs: list, values: list, space: int):
    dp = [0] * (space + 1)

    for i in range(n):  # 0-1 背包问题中，这两层循环不可以交换
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

j       0   1   2   3   4   5   6   7   space
dp[j]   -----------------------------
init    0   0   0   0   0   0   0   0
1       0   3   6   9   12  15  18  21
1+2     0   3   7   10  14  17  21  24
1+2+3   0   3   7   10  14  17  21  24
"""


def complete_back(n: int, costs: list, values: list, space: int):
    dp = [0] * (space + 1)

    for i in range(n):  # 完全背包问题中，这两层循环可以交换
        for j in range(space + 1):
            if j < costs[i]:
                continue  # 这里是 continue
            dp[j] = max(dp[j], dp[j - costs[i]] + values[i])
        print(dp)

    return dp[space]


# print(complete_back(3, [1, 2, 5], [3, 7, 15], 7))


"""
装满 0-1 背包

有 n 个物品，物品有两个属性
代价 cost
价值 value，
背包在容量 space 的限制下可以装物品的最 **小** 价值（要求背包必须装满）？

思路：初始化时将除 0 以外的数定义为 'inf'，代表背包无法装到这个容量，若题目改为最大，则初始化为 '-inf'，并将 min 改为 max 即可
假设物品数 n = 4  costs = [2, 3, 5, 7]  values = [3, 5, 7, 9]  space = 10

j       0   1   2   3   4   5   6   7   8   9   10
dp[j]   ------------------------------------------
init    0   inf inf inf inf inf inf inf inf inf inf
1       0   inf 3   inf inf inf inf inf inf inf inf
1+2     0   inf 3   5   inf 8   inf inf inf inf inf
1+2+3   0   inf 3   5   inf 7   inf 10  12  inf 15
1+2+3+4 0   inf 3   5   inf 7   inf 9   12  12  14
"""


def filled_zero_one_back(n: int, costs: list, values: list, space: int):
    dp = [float('inf')] * (space + 1)
    dp[0] = 0

    for i in range(n):  # 0-1 背包问题中，这两层循环不可以交换
        for j in reversed(range(space + 1)):
            if j < costs[i]:
                break  # 这里因为 j 是有序的（越来越小），所以可以用 break，否则用 continue
            dp[j] = min(dp[j], dp[j - costs[i]] + values[i])
        print(dp)

    return dp[space]


print(filled_zero_one_back(4, [2, 3, 5, 7], [3, 5, 7, 9], 10))


"""
装满完全背包

有 n 个物品，物品的数量无限，物品有两个属性
代价 cost
价值 value，
背包在容量 space 的限制下可以装物品的最 **小** 价值（要求背包必须装满）？

思路：初始化时将除 0 以外的数定义为 'inf'，代表背包无法装到这个容量，若题目改为最大，则初始化为 '-inf'，并将 min 改为 max 即可
假设物品数 n = 4  costs = [2, 3, 5, 7]  values = [3, 5, 7, 9]  space = 10

j       0   1   2   3   4   5   6   7   8   9   10
dp[j]   ------------------------------------------
init    0   inf inf inf inf inf inf inf inf inf inf
1       0   inf 3   inf 6   inf 9   inf 12  inf 15
1+2(1)  0   inf 3   5   6   inf 9   inf 12  15  15
1+2(2)  0   inf 3   5   6   8   9   11  12  14  15
1+2+3   0   inf 3   5   6   7   9   10  12  13  14
1+2+3+4 0   inf 3   5   6   7   9   9   12  12  14
"""


def filled_complete_back(n: int, costs: list, values: list, space: int):
    dp = [float('inf')] * (space + 1)
    dp[0] = 0

    for i in range(n):  # 完全背包问题中，这两层循环可以交换
        for j in range(space + 1):
            if j < costs[i]:
                continue  # 这里是 continue
            dp[j] = min(dp[j], dp[j - costs[i]] + values[i])
        print(dp)

    return dp[space]


# print(filled_complete_back(4, [2, 3, 5, 7], [3, 5, 7, 9], 10))
