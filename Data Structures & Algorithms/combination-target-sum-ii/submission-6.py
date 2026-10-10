class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, currSum, total):
            if total == target:
                res.append(currSum.copy())
                return
            if i == len(candidates) or total > target:
                return
            
            currSum.append(candidates[i])
            dfs(i+1, currSum, total + candidates[i])

            currSum.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, currSum, total)

        dfs(0, [], 0)
        return res