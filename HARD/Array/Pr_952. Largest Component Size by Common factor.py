from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        # path compression (iterative)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

class Solution:
    def largestComponentSize(self, nums):
        if not nums:
            return 0

        maxV = max(nums)
        dsu = DSU(maxV + 1)

        # Smallest prime factor sieve (spf)
        spf = list(range(maxV + 1))
        i = 2
        while i * i <= maxV:
            if spf[i] == i:
                j = i * i
                while j <= maxV:
                    if spf[j] == j:
                        spf[j] = i
                    j += i
            i += 1

        def prime_factors(x):
            # return distinct prime factors using spf
            factors = set()
            while x > 1:
                p = spf[x]
                factors.add(p)
                while x % p == 0:
                    x //= p
            return factors

        # Union each number with its prime factors
        for num in nums:
            for p in prime_factors(num):
                dsu.union(num, p)

        # Count component sizes only over the given nums
        count = defaultdict(int)
        ans = 0
        for num in nums:
            root = dsu.find(num)
            count[root] += 1
            if count[root] > ans:
                ans = count[root]

        return ans
