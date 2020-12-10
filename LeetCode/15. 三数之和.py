def threeSum(nums: list) -> list:
    res = []
    nums.sort()
    for first in range(len(nums)):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        target = -nums[first]
        left = first + 1
        right = len(nums) - 1
        while left < right:
            if left > first + 1 and nums[left] == nums[left - 1]:
                left += 1
                continue
            if nums[left] + nums[right] == target:
                res.append([nums[first], nums[left], nums[right]])
                left += 1
                continue
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
    return res


print(threeSum([-1, 0, 1, 1, 1, 1]))
        
