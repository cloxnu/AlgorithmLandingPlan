class Solution:
    def canPartition(self, nums: list) -> bool:
        # 纸上演算一下
        s = sum(nums)
        if s % 2 == 1:
            return False
        dp = [False for _ in range(s // 2 + 1)]
        dp[s // 2] = True
        for num in nums:
            for j in range(s // 2 + 1):
                if j + num > s // 2:
                    break
                dp[j] = dp[j] or dp[j + num]
                if j == 0 and dp[j]:
                    return True
        return False

