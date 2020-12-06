def firstUniqChar(s: str) -> str:
    visit = {}
    for i in s:
        if i in visit:
            visit[i] = True
        else:
            visit[i] = False
    for key, value in visit.items():
        if not value:
            return key
    return " "
