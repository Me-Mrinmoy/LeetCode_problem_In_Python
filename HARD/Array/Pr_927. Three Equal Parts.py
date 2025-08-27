class Solution(object):
    def threeEqualParts(self, arr):
        n = len(arr)
        total_ones = sum(arr)

        # All zeros → any split works
        if total_ones == 0:
            return [0, n - 1]

        # Must be divisible by 3
        if total_ones % 3 != 0:
            return [-1, -1]

        k = total_ones // 3  # ones per part

        # Find first '1' index of each part
        first = second = third = -1
        ones_seen = 0
        for i, bit in enumerate(arr):
            if bit == 1:
                ones_seen += 1
                if ones_seen == 1:
                    first = i
                elif ones_seen == k + 1:
                    second = i
                elif ones_seen == 2 * k + 1:
                    third = i
                    break

        # Compare the patterns until the end; they must match bit-by-bit
        while third < n and arr[first] == arr[second] == arr[third]:
            first += 1
            second += 1
            third += 1

        # If third reached n, segments match; compute indices
        if third == n:
            return [first - 1, second]

        return [-1, -1]
