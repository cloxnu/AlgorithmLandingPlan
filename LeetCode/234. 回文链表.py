class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        slow.next, slow = None, slow.next
        while slow:
            slow.next, mid.next, slow = mid.next, slow, slow.next
        node1 = head
        node2 = mid.next
        while node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True

