# 堆排序 时间 O(n log n) 空间 O(1)

# 调整堆（递归形式）
def heap_sort(nums: list) -> list:
    def adjust(heap: list, start, end):
        left = start * 2 + 1
        right = left + 1
        if start >= end or left >= end: return
        max_child = right if right < end and heap[left] < heap[right] else left  # 选取最大的子结点
        if heap[start] < heap[max_child]:
            heap[start], heap[max_child] = heap[max_child], heap[start]
            adjust(heap, max_child, end)

    # 从最后一个结点的父结点开始建堆
    for i in reversed(range(len(nums) // 2)):
        adjust(nums, i, len(nums))
    # 将最大结点交换至最后并调整堆
    for i in reversed(range(len(nums))):
        nums[0], nums[i] = nums[i], nums[0]
        adjust(nums, 0, i)
    return nums


# 调整堆（迭代形式）
def heap_sort_iter(nums: list) -> list:
    def adjust(heap: list, start, end):
        while start < end:
            left = start * 2 + 1
            right = left + 1
            if left >= end: break
            max_child = right if right < end and heap[left] < heap[right] else left  # 选取最大的子结点
            if heap[start] >= heap[max_child]: break
            heap[start], heap[max_child] = heap[max_child], heap[start]
            start = max_child

    # 从最后一个结点的父结点开始建堆
    for i in reversed(range(len(nums) // 2)):
        adjust(nums, i, len(nums))
    # 将最大结点交换至最后并调整堆
    for i in reversed(range(len(nums))):
        nums[0], nums[i] = nums[i], nums[0]
        adjust(nums, 0, i)
    return nums


print(heap_sort_iter([5, 6, 7, 8, 9, 0, 1, 2, 3, 4]))
