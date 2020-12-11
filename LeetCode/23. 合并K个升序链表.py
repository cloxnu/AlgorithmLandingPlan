class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list) -> ListNode:
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode(next=l1)
        compare2 = l2
        while curr.next and compare2:
            if curr.next.val > compare2.val:
                curr.next, compare2 = compare2, curr.next
            curr = curr.next
        if compare2:
            curr.next = compare2
        return dummy.next

    def recur(l: list):
        if len(l) == 0:
            return None
        if len(l) == 1:
            return l[0]
        mid = len(l) // 2
        return mergeTwoLists(recur(l[:mid]), recur(l[mid:]))

    return recur(lists)

