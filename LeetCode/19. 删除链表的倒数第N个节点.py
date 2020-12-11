# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(next=head)
    node_will_remove = node = dummy
    count = 0
    while node:
        node = node.next
        if count >= n+1:
            node_will_remove = node_will_remove.next
        count += 1
    node_will_remove.next = node_will_remove.next.next
    return dummy.next
