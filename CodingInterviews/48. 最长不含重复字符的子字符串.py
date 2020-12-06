def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0: return 0
    left = 0
    right = 0
    visit = {}
    res = 0
    while right < len(s):
        if s[right] in visit and visit[s[right]] >= left:
            left = visit[s[right]] + 1
        visit[s[right]] = right
        res = max(right - left + 1, res)
        right += 1
    return res
