def isValid(s: str) -> bool:
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
            continue
        if len(stack) == 0:
            return False
        if c == ')' and stack[-1] == '(' or c == ']' and stack[-1] == '[' or c == '}' and stack[-1] == '{':
            stack.pop()
        else:
            return False
    if len(stack) > 0:
        return False
    return True

