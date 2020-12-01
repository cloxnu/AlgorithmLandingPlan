# 归并，平均最差均为 O(n log n)，空间 O(n)

# 类似二叉树的 **后序** 遍历，先 recur 左右，再 visit 自己，所以迭代采用树的后序遍历模板

# 递归形式
def merge_sort(nums: list) -> list:
    def merge(l1: list, l2: list) -> list:
        res = []
        while l1 and l2:
            res.append(l1.pop(0) if l1[0] < l2[0] else l2.pop(0))
        res.extend(l1 if l1 else l2)
        return res

    def recur(nums: list) -> list:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        return merge(recur(nums[:mid]), recur(nums[mid:]))
    
    return recur(nums)


# 迭代形式
def merge_sort_iter(nums: list) -> list:
    def merge(l1: list, l2: list) -> list:
        res = []
        while l1 and l2:
            res.append(l1.pop(0) if l1[0] < l2[0] else l2.pop(0))
        res.extend(l1 if l1 else l2)
        return res

    # 类似树的后序遍历，stack 里不存 list 是因为这里每层迭代都需要上一次的结果，而不是缓存下来
    stack = [(0, len(nums))]
    res = []
    while stack:
        left, right = stack.pop()
        if left >= right - 1: continue
        mid = left + (right - left) // 2
        res.append((left, mid, right))
        stack.append((left, mid)) # 先入栈左半段
        stack.append((mid, right)) # 再入栈右半段
        
    for left, mid, right in reversed(res):
        nums[left:right] = merge(nums[left:mid], nums[mid:right])
    return nums


print(merge_sort_iter([4, 5, 3]))
