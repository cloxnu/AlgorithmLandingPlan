class ListNode:
    def __init__(self, val='0', next=None):
        self.val = val
        self.next = next

    def out(self):
        node = self
        count = 0
        while node:
            if count >= 100:
                print("太长了")
                return
            print(node.val, end=" ")
            node = node.next
            count += 1


a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
d = ListNode('d')
e = ListNode('e')
f = ListNode('f')

# a.next = b
# b.next = c
# c.next = d
# d.next = e

a.next, b.next, c.next, d.next = b, c, d, e

L = b
R = c

# L, R, R.next = R, R.next, L
R.next, L, R = L, R, R.next

c.out()
