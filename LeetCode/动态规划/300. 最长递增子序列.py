class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        dp = [1 for _ in nums]
        res = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])
        return res
