
# 堆

def getLeastNumbers(arr: list, k: int) -> list:
    def adjust(heap: list, start, end):
        left = start * 2 + 1
        right = left + 1
        if left >= end:
            return
        maxChild = right if right < end and heap[right] > heap[left] else left
        if heap[start] < heap[maxChild]:
            heap[start], heap[maxChild] = heap[maxChild], heap[start]
            adjust(heap, maxChild, end)

    if k == 0: return []
    if len(arr) == k: return arr
    heap = []
    heap += arr[:k]

    for i in reversed(range(0, len(heap)//2)):
        adjust(heap, i, len(heap))

    for i in range(k, len(arr)):
        if arr[i] < heap[0]:
            heap[0] = arr[i]
            adjust(heap, 0, len(heap))

    return heap

print(getLeastNumbers([3, 2, 1], 2))

