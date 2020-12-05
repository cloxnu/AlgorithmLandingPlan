def exchange(nums: list[int]) -> list[int]:
    left, right = 0, len(nums)-1
    while left < right:
        while nums[left] & 1:
            left += 1
            if left >= right:
                return nums
        while not nums[right] & 1:
            right -= 1
            if left >= right:
                return nums
        nums[left], nums[right] = nums[right], nums[left]
    return nums

print(exchange([1, 2, 3, 4, 5]))
