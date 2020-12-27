import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        indegree = [0 for _ in range(numCourses)]
        to = collections.defaultdict(list)

        for t, f in prerequisites:
            indegree[t] += 1
            to[f].append(t)

        res = []
        queue = [idx for idx in range(numCourses) if indegree[idx] == 0]
        while queue:
            idx = queue.pop(0)
            res.append(idx)
            for one in to[idx]:
                indegree[one] -= 1
                if indegree[one] == 0:
                    queue.append(one)
        return res if len(res) == numCourses else []

