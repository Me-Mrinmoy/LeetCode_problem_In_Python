class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        
        def countLessEqual(mid):
            count = 0
            row = n - 1
            col = 0
            
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count
        
        low, high = matrix[0][0], matrix[-1][-1]
        
        while low < high:
            mid = (low + high) // 2
            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid
        
        return low
