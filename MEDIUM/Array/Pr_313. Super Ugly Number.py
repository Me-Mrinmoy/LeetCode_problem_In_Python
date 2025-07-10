class Solution(object):                 # “object” keeps it Py‑2 compatible
    def nthSuperUglyNumber(self, n, primes):
        size = len(primes)

        uglies   = [1] * n              # super‑ugly numbers
        indices  = [0] * size           # next index for each prime
        candidates = primes[:]          # <-- shallow copy without .copy()

        for i in range(1, n):
            next_ugly = min(candidates)
            uglies[i] = next_ugly

            # update every prime that produced the minimum
            for j in range(size):
                if candidates[j] == next_ugly:
                    indices[j] += 1
                    candidates[j] = primes[j] * uglies[indices[j]]

        return uglies[-1]
