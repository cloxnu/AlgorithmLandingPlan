class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        deque = []
        res = []

        for i in range(len(nums)):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            if i >= k:
                if deque[0] == nums[i - k]:
                    deque.pop(0)
            if i >= k - 1:
                res.append(deque[0])

        return res
