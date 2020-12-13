def searchRange(nums: list, target: int) -> list:
    def search() -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def findStartAndEnd(idx):
        start = 0
        end = 0
        left = 0
        right = idx
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if mid - 1 < 0 or nums[mid - 1] != target:
                    start = mid
                    break
                right = mid - 1
            else:
                left = mid + 1
        else:
            start = idx

        left = idx
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if mid + 1 >= len(nums) or nums[mid + 1] != target:
                    end = mid
                    break
                left = mid + 1
            else:
                right = mid - 1
        else:
            end = idx

        return [start, end]

    idx = search()
    if idx == -1:
        return [-1, -1]
    return findStartAndEnd(idx)


print(searchRange([0, 0, 0, 7, 8], 7))




