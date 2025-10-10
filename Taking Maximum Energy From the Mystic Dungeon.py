Taking Maximum Energy From the Mystic Dungeon

from math import inf
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        
        # compute dp from rightmost magician backwards
        for i in range(n - 1, -1, -1):
            dp[i] = energy[i]
            jump_index = i + k
            if jump_index < n:
                dp[i] += dp[jump_index]
        
        # result is the best among all starting positions
        return max(dp)
