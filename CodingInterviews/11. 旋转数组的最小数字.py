# 二分查找
def minArray(numbers: list[int]) -> int:
    if len(numbers) == 0: return -1
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if numbers[mid] > numbers[right]:
            left = mid + 1
        elif numbers[mid] < numbers[right]:
            right = mid
        else:
            right -= 1
    return numbers[left]

print(minArray([1, 3, 5]))


# 普通的二分查找
def bin(numbers: list, searchnum) -> int:
    if len(numbers) == 0: return -1
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if numbers[mid] == searchnum:
            return mid
        elif numbers[mid] > searchnum:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# print(bin([2, 3, 4, 6, 8, 9], 1))
