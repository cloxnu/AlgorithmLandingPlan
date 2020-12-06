def twoSum(nums: list, target: int) -> list:
    left = 0
    right = len(nums) - 1
    while target != nums[left] + nums[right] and left < right:
        if target < nums[left] + nums[right]:
            right -= 1
        else:
            left += 1
    return [nums[left], nums[right]]
