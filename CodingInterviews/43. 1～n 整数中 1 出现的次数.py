def countDigitOne(n: int) -> int:
    digit = 1
    res = 0
    while n // digit != 0:
        high = n // (digit * 10)
        low = n % digit
        curr = (n // digit) % 10
        print(high, curr, low)
        if curr == 0:
            res += high * digit
        elif curr == 1:
            res += high * digit + low + 1
        else:
            res += high * digit + digit
        digit *= 10
    return res


print(countDigitOne(1231))
