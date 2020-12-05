# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
    currNode = head
    desNode = None
    count = 0
    while currNode:
        currNode = currNode.next
        count += 1
        if count == k:
            desNode = head
        if count > k:
            desNode = desNode.next
    return desNode

