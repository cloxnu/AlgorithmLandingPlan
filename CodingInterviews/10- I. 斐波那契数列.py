def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prepre = 0
        pre = 1
        curr = 0
        for _ in range(2, n+1):
            curr = pre + prepre
            prepre = pre
            pre = curr
        return curr

print(fib(45))
