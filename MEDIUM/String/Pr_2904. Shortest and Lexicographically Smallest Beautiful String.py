#Python
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ""
        
        l = 0
        r = 0
        ones = 0
        min_len = len(s) + 1
        ans = ""
        n = len(s)
        
        while r < n:
            if s[r] == '1':
                ones += 1
                
            while l < r and ones > k:
                if s[l] == '1':
                    ones -= 1
                l += 1
                
            while l < r and s[l] == '0':
                l += 1
                
            if ones == k:
                curr_len = r - l + 1
                curr = s[l : r + 1]
                if min_len > curr_len:
                    min_len = curr_len
                    ans = curr
                elif min_len == curr_len:
                    if curr < ans:
                        ans = curr
            r += 1
            
        return ans
