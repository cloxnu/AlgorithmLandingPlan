class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: 'Node') -> 'Node':
    copied = {}

    def generate(node: Node) -> Node:
        if node is None: return None
        if node in copied:
            return copied[node]
        newNode = Node(node.val)
        copied[node] = newNode
        newNode.next = generate(node.next)
        newNode.random = generate(node.random)
        return newNode

    return generate(head)
