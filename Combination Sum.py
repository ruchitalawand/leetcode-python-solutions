Combination Sum

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start, path, total):
            # Base cases
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            # Explore further candidates
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # allow reuse of same element
                path.pop()  # backtrack

        backtrack(0, [], 0)
        return res
