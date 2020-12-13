class Solution:
    def trap(self, height: list) -> int:
        left, right = 0, len(height) - 1
        left_m, right_m = 0, 0
        res = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] < left_m:
                    res += left_m - height[left]
                else:
                    left_m = height[left]
                left += 1
            else:
                if height[right] < right_m:
                    res += right_m - height[right]
                else:
                    right_m = height[right]
                right -= 1
        return res

    def trap2(self, height: list) -> int:
        stack = []
        left, right = [-1 for _ in height], [len(height) for _ in height]
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                right[top] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        res = 0
        for i in range(len(height)):
            if left[i] < 0 or right[i] >= len(height):
                continue
            res += (right[i] - left[i] - 1) * (min(height[left[i]], height[right[i]]) - height[i])
        return res
