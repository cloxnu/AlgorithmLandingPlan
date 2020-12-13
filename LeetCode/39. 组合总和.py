class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        def dfs(idx, target):
            if target == 0:
                res.append(combination[:])
                return
            if idx >= len(candidates):
                return
            dfs(idx + 1, target)
            if target - candidates[idx] >= 0:
                combination.append(candidates[idx])
                dfs(idx, target - candidates[idx])
                combination.pop()
        dfs(0, target)
        return res