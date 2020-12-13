class Solution:
    def subsets(self, nums: list) -> list:
        res = []
        combination = []
        def comb(start, end, count, reduce):
            if count <= 0:
                combination.append(reduce)
                return
            if end - start < count:
                return
            for j in range(start, end):
                comb(j + 1, end, count - 1, reduce + [nums[j]])
        for i in range(len(nums) + 1):
            combination = []
            comb(0, len(nums), i, [])
            res += combination
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
