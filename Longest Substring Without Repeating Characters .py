Longest Substring Without Repeating Characters 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}       # char -> last index seen
        left = 0             # left index of current window
        max_len = 0

        for right, ch in enumerate(s):
            # if ch was seen and is inside current window, move left
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            # window is s[left:right+1]
            max_len = max(max_len, right - left + 1)

        return max_len

        
