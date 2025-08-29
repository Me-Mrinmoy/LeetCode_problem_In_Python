class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        deletions = 0
        # sorted_pair[i] == True means strs[i] < strs[i+1] already confirmed
        sorted_pair = [False] * (n - 1)

        for col in range(m):
            # If this column causes an inversion for any unconfirmed pair -> delete it
            must_delete = False
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] > strs[i+1][col]:
                    must_delete = True
                    break
            if must_delete:
                deletions += 1
                continue

            # Otherwise, keep the column and mark newly confirmed pairs
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] < strs[i+1][col]:
                    sorted_pair[i] = True

            # If all adjacent pairs are confirmed sorted, we can stop early
            if all(sorted_pair):
                break

        return deletions
