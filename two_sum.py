# LeetCode 1. Two Sum
# Problem: https://leetcode.com/problems/two-sum/
# Time: O(n), Space: O(n)

class Solution:
    def twoSum(self, nums, target):
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], i]
            hash_map[num] = i
