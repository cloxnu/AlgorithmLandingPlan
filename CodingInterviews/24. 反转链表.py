
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(self, head: ListNode) -> ListNode:
    if head is None: return head
    node = head.next
    head.next = None
    while node:
        temp = node
        node = node.next
        temp.next = head
        head = temp
    return head

