class Solution:
    def lenLongestFibSubseq(self, arr):
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        dp = {}
        max_len = 0
        
        for j in range(n):
            for i in range(j):
                prev = arr[j] - arr[i]
                if prev < arr[i] and prev in index:
                    k = index[prev]
                    dp[(i,j)] = dp.get((k,i), 2) + 1
                    max_len = max(max_len, dp[(i,j)])
                else:
                    dp[(i,j)] = 2
        
        return max_len if max_len >= 3 else 0
