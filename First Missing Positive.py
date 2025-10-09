 First Missing Positive

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # Place each number in its right place (nums[i] -> nums[nums[i]-1])
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        # Find the first index where number is wrong
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # All numbers from 1..n are in place
        return n + 1
