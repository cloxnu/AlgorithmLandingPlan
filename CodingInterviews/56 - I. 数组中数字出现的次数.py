def singleNumbers(nums: list) -> list:
    s = 0
    for i in nums:
        s ^= i
    div = 1
    while s & div == 0:
        div <<= 1
    a, b = 0, 0
    for i in nums:
        if i & div == 0:
            a ^= i
        else:
            b ^= i
    return [a, b]


