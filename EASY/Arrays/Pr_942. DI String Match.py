class Solution:
    def diStringMatch(self, s):
        n = len(s)
        low, high = 0, n
        res = []
        
        for ch in s:
            if ch == 'I':
                res.append(low)
                low += 1
            else:  # 'D'
                res.append(high)
                high -= 1
        
        res.append(low)  # low == high at the end
        return res
