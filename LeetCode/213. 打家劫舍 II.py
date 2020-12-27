class Solution:
    def rob(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        r, nr = 0, 0
        for i in range(len(nums) - 1):
            r, nr = nr + nums[i], max(r, nr)
        res1 = max(r, nr)
        r, nr = 0, 0
        for i in range(1, len(nums)):
            r, nr = nr + nums[i], max(r, nr)
        res2 = max(r, nr)
        return max(res1, res2)
