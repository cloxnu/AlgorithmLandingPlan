# 归并，平均最差均为 O(n log n)，空间 O(n)

# 类似二叉树的 **后序** 遍历，先 recur 左右，再 visit 自己，所以迭代

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


print(merge_sort([5, 6, 7, 8, 9, 0, 1, 2, 3, 4]))
