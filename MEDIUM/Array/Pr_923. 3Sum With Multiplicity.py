from collections import Counter

class Solution:
    def threeSumMulti(self, arr, target):
        MOD = 10**9 + 7
        freq = Counter(arr)
        keys = sorted(freq)
        
        res = 0
        for i in range(len(keys)):
            x = keys[i]
            for j in range(i, len(keys)):
                y = keys[j]
                z = target - x - y
                if z < y:  # ensure order x <= y <= z
                    continue
                if z not in freq:
                    continue
                
                # Case 1: x == y == z
                if x == y == z:
                    c = freq[x]
                    res += c * (c - 1) * (c - 2) // 6
                
                # Case 2: x == y != z
                elif x == y != z:
                    c1, c2 = freq[x], freq[z]
                    res += c1 * (c1 - 1) // 2 * c2
                
                # Case 3: x != y == z
                elif x != y and y == z:
                    c1, c2 = freq[x], freq[y]
                    res += c1 * c2 * (c2 - 1) // 2
                
                # Case 4: all different
                else:  # x < y < z
                    res += freq[x] * freq[y] * freq[z]
        
        return res % MOD
