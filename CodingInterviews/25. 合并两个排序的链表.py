class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2:
        return l1 if l1 else l2
    dummy = ListNode(None)
    dummy.next = l1
    node1l, node1r, node2 = dummy, l1, l2
    while node1r and node2:
        if node1r.val >= node2.val and (node1l.val is None or (node1l.val is not None and node2.val >= node1l.val)):
            newNode = ListNode(node2.val)
            newNode.next = node1r
            node1l.next = newNode
            node1l = node1l.next
            node2 = node2.next
        else:
            node1r = node1r.next
            node1l = node1l.next
    while node2:
        newNode = ListNode(node2.val)
        node1l.next = newNode
        node1l = node1l.next
        node2 = node2.next
    return dummy.next

# 没那么复杂，啥时候再写一遍
