from collections import Counter, defaultdict

class Solution:
    def isPossible(self, nums):
        count = Counter(nums)       # Frequency of each number
        end = defaultdict(int)      # Number of subsequences ending at a number

        for num in nums:
            if count[num] == 0:
                continue

            # Use this number
            count[num] -= 1

            # Case 1: Extend a sequence ending at num-1
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1

            # Case 2: Start a new sequence num, num+1, num+2
            elif count[num + 1] > 0 and count[num + 2] > 0:
                count[num + 1] -= 1
                count[num + 2] -= 1
                end[num + 2] += 1

            # Case 3: Not possible
            else:
                return False

        return True
