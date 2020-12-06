def missingNumber(nums: list) -> int:
    if nums[0] == 1: return 0

    def search(left, right):
        if left >= right - 1:
            return left + 1
        mid = left + (right - left) // 2
        if nums[mid] > mid:
            return search(left, mid)
        else:
            return search(mid, right)

    return search(0, len(nums))
