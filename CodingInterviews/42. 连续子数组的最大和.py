def maxSubArray(nums: list) -> int:
    for i in range(len(nums)):
        nums[i] = nums[i - 1] + nums[i] if i >= 1 and nums[i - 1] >= 0 else nums[i]
    return max(nums)

