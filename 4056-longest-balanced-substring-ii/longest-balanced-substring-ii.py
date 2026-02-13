from collections import defaultdict

class Solution:
    def helper(self, s: str, ch1: str, ch2: str) -> int:
        n = len(s)
        diff_map = {}
        max_len = 0
        count1 = 0
        count2 = 0
        
        for i in range(n):
            if s[i] != ch1 and s[i] != ch2:
                diff_map.clear()
                count1 = 0
                count2 = 0
                continue
            
            if s[i] == ch1:
                count1 += 1
            if s[i] == ch2:
                count2 += 1
            
            if count1 == count2:
                max_len = max(max_len, count1 + count2)
            
            diff = count1 - count2
            if diff in diff_map:
                max_len = max(max_len, i - diff_map[diff])
            else:
                diff_map[diff] = i
        
        return max_len
    
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        # Case-1: consecutive same characters
        count = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 1
        max_len = max(max_len, count)
        
        # Case-2: two-character balance
        max_len = max(max_len, self.helper(s, 'a', 'b'))
        max_len = max(max_len, self.helper(s, 'a', 'c'))
        max_len = max(max_len, self.helper(s, 'b', 'c'))
        
        # Case-3: three-character balance
        countA = countB = countC = 0
        diff_map = {}
        
        for i in range(n):
            if s[i] == 'a':
                countA += 1
            elif s[i] == 'b':
                countB += 1
            elif s[i] == 'c':
                countC += 1
            
            if countA == countB == countC:
                max_len = max(max_len, countA + countB + countC)
            
            key = (countA - countB, countA - countC)
            if key in diff_map:
                max_len = max(max_len, i - diff_map[key])
            else:
                diff_map[key] = i
        
        return max_len


# Example usage:
sol = Solution()
s = "aaabbbcccabcabc"
print(sol.longestBalanced(s))  # Output depends on input string
