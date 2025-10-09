Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        # Get previous term
        prev = self.countAndSay(n - 1)
        result = ""
        count = 1

        # Build current term by counting consecutive digits
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]
                count = 1
        
        # Append the last counted group
        result += str(count) + prev[-1]
        return result
