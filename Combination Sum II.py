Combination Sum II 

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()  # Sort to handle duplicates easily

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            prev = -1  # Track duplicate elements
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue  # Skip duplicates
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # Move to next index (no reuse)
                path.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return res
