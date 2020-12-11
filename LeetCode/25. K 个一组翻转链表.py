class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    def reverseLinkedList(head: ListNode, tail: ListNode):
        left = head
        right = head.next
        while left != tail:
            # right, right.next, left = left, right, right.next
            # left, right.next, right = right.next, right, left
            left, right.next, right = right, left, right.next
            # p = right
            # right = right.next
            # p.next = left
            # left = p
        return tail, head

    left = right = dummy = ListNode(next=head)
    while right:
        for _ in range(k):
            right = right.next
            if right is None:
                return dummy.next
        next_head = right.next
        after_left, before_right = reverseLinkedList(left.next, right)
        print(after_left.val, before_right.val)
        left.next, before_right.next = after_left, next_head
        right = left = before_right


print(reverseKGroup(ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5))))), 2))

