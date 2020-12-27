class Solution:
    def rob(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in nums]
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]

    def rob2(self, nums: list) -> int:
        r, nr = 0, 0
        for i in range(len(nums) - 1):
            r, nr = nr + nums[i], max(r, nr)
        return max(r, nr)
