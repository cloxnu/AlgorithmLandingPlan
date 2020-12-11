def generateParenthesis(n: int) -> list:
    if n == 0:
        return ['']
    res = []
    for i in range(n):
        for left in generateParenthesis(i):
            for right in generateParenthesis(n-i-1):
                res.append("({}){}".format(left, right))
    return res

print(generateParenthesis(3))
