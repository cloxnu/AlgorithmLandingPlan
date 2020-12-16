# 并查集

"""
[并查集](https://ds.an.dog/content/V.%E6%A0%91/5.10-%E9%9B%86%E5%90%88%E8%A1%A8%E7%A4%BA.html)

实现「加权规则」和「折叠规则」

使用并查集，轻松秒掉
[200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

本算法时间复杂度为 O(nα(n)). α(n) 是反阿克曼函数，当自变量 n 的值在人类可观测的范围内（宇宙中粒子的数量）时，函数 α(n) 的值不会超过 5，因此也可以看成是常数时间复杂度。

"""

class UnionFind:
    def __init__(self, all_data: list):
        """
        初始化并查集
        :param all_data: 数据列表
        """
        self.parent = {}
        self.size = {}
        self.union_num = 0

        for data in all_data:
            self.parent[data] = data  # 初始父亲结点为自己
            self.size[data] = 1
            self.union_num += 1

    def __repr__(self):
        return "parent: {}\nsize: {}\nunion_num: {}\n".format(self.parent, self.size, self.union_num)

    def add(self, *will_add_data):
        for data in will_add_data:
            if data not in self.parent:
                self.parent[data] = data
                self.size[data] = 1
                self.union_num += 1

    def find(self, data):
        """
        查找 data 属于哪个集合，返回 root
        :param data: 要查询的值
        :return: data 属于的集合的 root
        """
        if data not in self.parent:
            return None
        node = data  # 防止引用类型的 data 被改变
        nodes = []  # 将路上的 node 全部记下来
        while self.parent[node] != node:
            nodes.append(node)
            node = self.parent[node]
        for n in nodes:  # 将路上的 node 的父结点全部指向根结点以满足「折叠规则」
            self.parent[n] = node
            self.size[n] = 1
        return node

    def union(self, *will_union_data):
        """
        合并多个值，当值不存在时跳过
        :param will_union_data: 要合并的值
        """
        root1 = None  # 第一个要合并集合的 root
        for data in will_union_data:
            root2 = self.find(data)
            if root1 is None:
                root1 = root2  # 将 will_union_data 中第一个 data 的 root 赋值给 root1
            if root2 is None or root1 == root2:
                continue
            # size 小的集合合并到 size 大的集合
            if self.size[root1] >= self.size[root2]:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]
            else:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]
                root1 = root2  # 更新 root1 为新的 root
            self.union_num -= 1

    # deprecated
    def union2(self, data1, data2):
        """
        （已废弃）合并两个值，当值不存在时不合并
        :param data1: 要合并的第一个值
        :param data2: 要合并的第二个值
        """
        root1 = self.find(data1)
        root2 = self.find(data2)
        if root1 is None or root2 is None or root1 == root2:
            return
        # size 小的集合合并到 size 大的集合
        if self.size[root1] >= self.size[root2]:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]


if __name__ == '__main__':
    # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    union_find = UnionFind(nums)
    union_find.union(8, 9)
    union_find.union(7, 8)
    union_find.union(6, 7)
    union_find.union(5, 6)
    union_find.union(4, 5)
    union_find.union(3, 4)
    union_find.union(2, 3)
    union_find.union(1, 2)
    union_find.union(0, 1)
    print(union_find)

