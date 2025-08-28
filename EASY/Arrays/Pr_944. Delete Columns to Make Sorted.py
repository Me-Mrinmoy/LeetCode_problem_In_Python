class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        delete_count = 0

        for col in range(m):
            for row in range(n - 1):
                if strs[row][col] > strs[row + 1][col]:
                    delete_count += 1
                    break  # no need to check further rows for this column

        return delete_count
