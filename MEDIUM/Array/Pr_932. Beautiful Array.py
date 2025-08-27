class Solution:
    def beautifulArray(self, n):
        res = [1]
        while len(res) < n:
            res = [x * 2 - 1 for x in res if x * 2 - 1 <= n] + \
                  [x * 2 for x in res if x * 2 <= n]
        return res
