def maxSlidingWindow(nums: list, k: int) -> list:
    queue = []
    res = []
    for i in range(0, len(nums)):
        if i >= k and nums[i - k] == queue[0]:
            queue.pop(0)
        while queue and queue[-1] < nums[i]:
            queue.pop()
        queue.append(nums[i])
        if i >= k - 1:
            res.append(queue[0])
    return res

print(maxSlidingWindow([1, 3, 8, 9, 6, 5, 3, 4, 2], 3))

