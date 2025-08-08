class Solution:
    def constructArray(self, n, k):
        res = []
        left, right = 1, n
        while left <= right:
            if k > 1:
                if k % 2 == 1:  # odd k → take from left
                    res.append(left)
                    left += 1
                else:           # even k → take from right
                    res.append(right)
                    right -= 1
                k -= 1
            else:
                res.append(left)
                left += 1
        return res
