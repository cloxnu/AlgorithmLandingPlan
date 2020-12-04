# 手撕快排
# 此方法为原地快排，平均 O(n log n)，最差 O(n^2), 最差情况为 [9, 8, 7, 6, 5, 4, 3, 2, 1]
# 网上双指针方法最差情况为 [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]

# 类似二叉树的 **前序** 遍历，先 visit 自己，再 recur 左右，所以迭代用栈替代即可

# 递归形式
def quick_sort(nums: list):
    def partition(left, right):
        store = left
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]
        return store

    def recur(left, right):
        if left >= right: return
        store = partition(left, right)
        recur(left, store - 1)
        recur(store + 1, right)

    recur(0, len(nums) - 1)
    return nums

# 迭代形式
def quick_sort_iter(nums: list):
    def partition(left, right):
        store = left
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]
        return store

    stack = [(0, len(nums) - 1)]
    while stack:
        left, right = stack.pop()
        if left >= right: continue
        store = partition(left, right)
        stack.append((store + 1, right))
        stack.append((left, store - 1))

    return nums


# print(quick_sort([2, 2, 2, 2, 4, 3, 5, 2, 6]))
print(quick_sort_iter([5, 6, 7, 8, 9, 0, 1, 2, 3, 4]))
# print(quick_sort_iter([1, 2, 1, 2, 1, 2, 1, 2, 1, 2]))
