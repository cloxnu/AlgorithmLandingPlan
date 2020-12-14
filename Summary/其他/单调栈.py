# 单调栈思想

"""
为什么要用单调栈？单调栈的作用是什么？
# 单调栈能在 O(n) 时间内找到一个 list 中所有值左边第一次比它大/小的元素和右边第一个比它大/小的元素

举个例子
[2, 3, 4, 7, 8, 6, 0, 1]
"2" 右边第一个比它小的元素是 "0", "6" 右边第一个比它小的元素是 "0" 左边第一个比它小的元素是 "4"

以下 left right 数组存的是左边比当前元素大/小的元素的下标，右边比当前元素大/小的元素的下标

若要求左右边比原数小的值，则用单调递增栈
得到的 left right 数组是 (-1 代表左边没有更小的了，8 代表右边没有更小的了)
left = [-1, 0, 1, 2, 3, 2, -1, 6]
right = [6, 6, 6, 5, 5, 6, 8, 8]

若要求左右边比原数大的值，则用单调递减栈
得到的 left right 数组是 (-1 代表左边没有更大的了，8 代表右边没有更大的了)
left = [-1, -1, -1, -1, -1, 4, 5, 5]
right = [1, 2, 3, 4, 8, 8, 7, 8]


它们的应用在这里
[42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water)
[84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram)
"""


# 单调递增栈：找左右比当前元素小的元素
def mono_increasing_stack(nums: list) -> (list, list):
    stack = []
    left, right = [-1] * len(nums), [len(nums)] * len(nums)  # 默认左边全为 -1，右边全为 8
    for i in range(len(nums)):
        while stack and nums[stack[-1]] > nums[i]:  # 当当前元素非递增了，就 pop 栈顶元素
            top = stack.pop()
            right[top] = i  # 当前元素把 top 弹出来了，说明当前元素是 top 右边第一个比它小的元素
        left[i] = stack[-1] if stack else -1  # 当前左边第一个比它小的元素就是栈里剩下它弹不了的元素了，如果栈空了，那左边就没有更小的了
        stack.append(i)
    return left, right


# 单调递减栈：找左右比当前元素大的元素
def mono_decreasing_stack(nums: list) -> (list, list):
    stack = []
    left, right = [-1] * len(nums), [len(nums)] * len(nums)
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            top = stack.pop()
            right[top] = i
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    return left, right


print(mono_decreasing_stack([2, 3, 4, 7, 8, 6, 0, 1]))
