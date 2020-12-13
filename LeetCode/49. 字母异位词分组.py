class Solution:
    def groupAnagrams(self, strs: list) -> list:
        res, dic, count = [], {}, 0
        for s in strs:
            sort = tuple(sorted(s))
            if sort in dic:
                res[dic[sort]].append(s)
            else:
                dic[sort] = count
                count += 1
                res.append([s])
        return res

