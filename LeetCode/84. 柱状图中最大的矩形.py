class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        stack = []
        left, right = [-1 for _ in heights], [len(heights) for _ in heights]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                curr = stack.pop()
                right[curr] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        return max([(right[i] - left[i] - 1) * heights[i] for i in range(len(heights))]) if heights else 0

