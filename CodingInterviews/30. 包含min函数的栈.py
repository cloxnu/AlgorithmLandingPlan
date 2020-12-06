class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.substack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if (not self.substack) or (self.substack and self.substack[-1] >= x):
            self.substack.append(x)

    def pop(self) -> None:
        if self.stack:
            v = self.stack.pop()
            if self.substack and v == self.substack[-1]:
                self.substack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def min(self) -> int:
        return self.substack[-1] if self.substack else None
