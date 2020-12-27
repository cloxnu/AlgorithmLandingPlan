
# 0:00
def quick_sort(nums: list):
    def partition(left, right):
        store = left
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]
        return store

    def recur(left, right):
        if left >= right:
            return
        store = partition(left, right)
        recur(left, store - 1)
        recur(store + 1, right)

    recur(0, len(nums)-1)
    return nums


# 3:22

def quick_sort_iter(nums: list):
    def partition(left, right):
        store = left
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]
        return store

    stack = [(0, len(nums)-1)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        store = partition(left, right)
        stack.append((store + 1, right))
        stack.append((left, store - 1))
    return nums

# 6:58

def merge_sort(nums: list):
    def merge(l1: list, l2: list):
        res = []
        while l1 and l2:
            res.append(l1.pop(0) if l1[0] < l2[0] else l2.pop(0))
        res.extend(l1 if l1 else l2)
        return res

    def recur(nums: list):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        return merge(recur(nums[:mid]), recur(nums[mid:]))

    return recur(nums)

# 13:50


def merge_sort_iter(nums: list):
    def merge(l1: list, l2: list):
        res = []
        while l1 and l2:
            res.append(l1.pop(0) if l1[0] < l2[0] else l2.pop(0))
        res.extend(l1 if l1 else l2)
        return res

    stack = [(0, len(nums))]
    res = []
    while stack:
        left, right = stack.pop()
        if left >= right - 1:
            continue
        mid = left + (right - left) // 2
        res.append((left, mid, right))
        stack.append((left, mid))
        stack.append((mid, right))
    for left, mid, right in reversed(res):
        nums[left:right] = merge(nums[left:mid], nums[mid:right])
    return nums

# 19:54

def heap_sort(nums: list):
    def adjust(heap: list, start, end):
        left = start * 2 + 1
        right = left + 1
        if left >= end:
            return
        max_child = right if right < end and heap[right] > heap[left] else left
        if heap[max_child] > heap[start]:
            heap[max_child], heap[start] = heap[start], heap[max_child]
            adjust(heap, max_child, end)

    for i in reversed(range(len(nums) // 2)):
        adjust(nums, i, len(nums))
    for i in reversed(range(len(nums))):
        nums[0], nums[i] = nums[i], nums[0]
        adjust(nums, 0, i)
    return nums


# 33:49

def heap_sort_iter(nums: list):
    def adjust(heap: list, start, end):
        while start < end:
            left = start * 2 + 1
            right = left + 1
            if left >= end:
                break
            max_child = right if right < end and heap[right] > heap[left] else left
            if heap[max_child] < heap[start]:
                break
            heap[max_child], heap[start] = heap[start], heap[max_child]
            start = max_child

    for i in reversed(range(len(nums) // 2)):
        adjust(nums, i, len(nums))
    for i in reversed(range(len(nums))):
        nums[i], nums[0] = nums[0], nums[i]
        adjust(nums, 0, i)
    return nums


# 40:24


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def visit(self):
        print(self.value, end=" ")  # 访问当前结点

test = TreeNode('A', left=TreeNode('B', left=TreeNode('D'), right=TreeNode('E')),
                right=TreeNode('C', left=TreeNode('F', left=TreeNode('H'), right=TreeNode('I')), right=TreeNode('G')))


def preorder(root: TreeNode):
    if root is None:
        return
    stack = []
    node = root
    while node or stack:
        while node:
            node.visit()
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right

# 50:00


def inorder(root: TreeNode):
    if root is None:
        return
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        node.visit()
        node = node.right

# 52:03

def postorder(root: TreeNode):
    if root is None:
        return
    stack = []
    res = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            res.append(node)
            node = node.right
        node = stack.pop()
        node = node.left
    for node in reversed(res):
        node.visit()


# 54:19

postorder(test)


def mono_decreasing_stack(nums: list) -> (list, list):
    left, right = [-1 for _ in nums], [len(nums) for _ in nums]
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            right[idx] = i
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    return left, right


# 1:01:34

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    def reverse(one_head: ListNode, one_tail: ListNode):
        pre, curr = None, one_head
        while pre != one_tail:
            curr.next, pre, curr = pre, curr, curr.next
        return one_tail, one_head

    pre = dummy = ListNode(0, next=head)
    curr = head
    while curr:
        for _ in range(k-1):
            curr = curr.next
            if curr is None:
                return dummy.next
        one_head, one_tail, curr = pre.next, curr, curr.next
        one_head, one_tail = reverse(one_head, one_tail)
        pre.next, one_tail.next = one_head, curr
        pre = one_tail
    return dummy.next

# 1:15:34


def mergeKLists(lists: list) -> ListNode:
    def merge(l1: ListNode, l2: ListNode):
        n1 = dummy = ListNode(0, next=l1)
        n2 = l2
        while n1.next and n2:
            if n1.next.val > n2.val:
                n1.next, n2 = n2, n1.next
            n1 = n1.next
        if n2:
            n1.next = n2
        return dummy.next

    def recur(lists: list):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        return merge(recur(lists[:mid]), recur(lists[mid:]))

    return recur(lists)

# 1:21:04
