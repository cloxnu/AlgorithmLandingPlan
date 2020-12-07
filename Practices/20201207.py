def quick_sort(nums: list) -> list:
    def partition(left, right):
        store = 0
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]
        return store

    def recur(left, right):
        if left >= right:
            return
        store = partition(left, right)
        recur(left, store - 1)
        recur(store + 1, right)

    recur(0, len(nums) - 1)
    return nums

# 3:35

def quick_sort_iter(nums: list) -> list:
    def partition(left, right):
        store = 0
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]
        return store

    stack = [(0, len(nums) - 1)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        store = partition(left, right)
        stack.append((store + 1, right))
        stack.append((left, store - 1))
    return nums

# 9:24

def merge_sort(nums: list) -> list:
    def merge(l1: list, l2: list) -> list:
        res = []
        while l1 and l2:
            res.append(l1.pop(0) if l1[0] <= l2[0] else l2.pop(0))
        res.extend(l1 if l1 else l2)
        return res

    def recur(l: list):
        if len(l) <= 1:
            return l
        mid = len(l) // 2
        return merge(recur(l[:mid]), recur(l[mid:]))

    return recur(nums)

# 13:41


def merge_sort_iter(nums: list) -> list:
    def merge(l1: list, l2: list) -> list:
        res = []
        while l1 and l2:
            res.append(l1.pop(0) if l1[0] <= l2[0] else l2.pop(0))
        res.extend(l1 if l1 else l2)
        return res

    stack = [(0, len(nums))]
    res = []
    while stack:
        left, right = stack.pop()
        if left >= right - 1:
            continue
        mid = left + (right - left) // 2
        res.append((left, mid, right))
        stack.append((mid, right))
        stack.append((left, mid))
    for left, mid, right in reversed(res):
        nums[left:right] = merge(nums[left:mid], nums[mid:right])
    return nums

# 20:40


def heap_sort(nums: list) -> list:
    def adjust(heap: list, start, end):
        left = start * 2 + 1
        right = left + 1
        if left >= end:
            return
        maxChild = right if right < end and heap[right] > heap[left] else left
        if heap[maxChild] > heap[start]:
            heap[maxChild], heap[start] = heap[start], heap[maxChild]
            adjust(heap, maxChild, end)

    for i in reversed(range(0, len(nums) // 2)):
        adjust(nums, i, len(nums))
    for i in reversed(range(0, len(nums))):
        nums[0], nums[i] = nums[i], nums[0]
        adjust(nums, 0, i)
    return nums

# 26:14


def heap_sort_iter(nums: list) -> list:
    def adjust(heap: list, start, end):
        while True:
            left = start * 2 + 1
            right = left + 1
            if left >= end:
                break
            maxChild = right if right < end and heap[right] >= heap[left] else left
            if nums[maxChild] < nums[start]:
                break
            nums[maxChild], nums[start] = nums[start], nums[maxChild]
            start = maxChild

    for i in reversed(range(0, len(nums) // 2)):
        adjust(nums, i, len(nums))
    for i in reversed(range(0, len(nums))):
        nums[0], nums[i] = nums[i], nums[0]
        adjust(nums, 0, i)
    return nums

# 31:35


print(heap_sort_iter([5, 6, 7, 1, 2, 3, 4, 5, 6, 7]))
