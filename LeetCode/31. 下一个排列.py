def nextPermutation(nums: list) -> None:
    last = None
    left_idx = None
    for idx in reversed(range(len(nums))):
        if last is None:
            last = nums[idx]
        if last > nums[idx]:
            left_idx = idx
            break
        else:
            last = nums[idx]
    else:
        nums.reverse()
        return
    for idx in reversed(range(left_idx+1, len(nums))):
        if nums[idx] > nums[left_idx]:
            nums[idx], nums[left_idx] = nums[left_idx], nums[idx]
            nums[left_idx+1:] = reversed(nums[left_idx+1:])
            break

