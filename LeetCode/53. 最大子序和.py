class Solution:
    def maxSubArray(self, nums: list) -> int:
        dp = [0 for _ in nums]
        m = float('-inf')
        for idx in range(len(nums)):
            dp[idx] = nums[idx]
            if idx != 0 and dp[idx - 1] >= 0:
                dp[idx] += dp[idx - 1]
            m = max(m, dp[idx])
        return m
