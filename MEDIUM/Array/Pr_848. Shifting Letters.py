class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        res = []
        total_shift = 0
        
        # process shifts in reverse (suffix sums)
        for i in range(n-1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26
            # shift current char
            new_char = chr((ord(s[i]) - ord('a') + total_shift) % 26 + ord('a'))
            res.append(new_char)
        
        return ''.join(reversed(res))
