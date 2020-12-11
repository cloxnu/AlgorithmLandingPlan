class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    left = right = dummy = ListNode(next=head)
    while right:
        for _ in range(2):
            right = right.next
            if right is None:
                return dummy.next
        # after_right = right.next
        # after_left = left.next
        # after_left.next = after_right
        # left.next = right
        # right.next = after_left
        # right = left

        left.next.next, left.next, right.next, left, right = right.next, right, left.next, left.next, left.next
    return dummy.next

