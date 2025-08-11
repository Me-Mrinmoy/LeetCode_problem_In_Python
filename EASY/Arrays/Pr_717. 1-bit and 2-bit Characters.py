class Solution:
    def isOneBitCharacter(self, bits):
        i = 0
        n = len(bits)
        while i < n - 1:   # stop before the last bit
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1

# quick local test (works in both Py2 and Py3)
if __name__ == "__main__":
    print(Solution().isOneBitCharacter([1,0,0]))   # True
    print(Solution().isOneBitCharacter([1,1,1,0])) # False
