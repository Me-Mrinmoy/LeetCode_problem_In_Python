class Solution:
    def matrixReshape(self, mat, r, c):
        flat = [num for row in mat for num in row]
        if len(flat) != r * c:
            return mat
        
        reshaped = []
        for i in range(0, len(flat), c):
            reshaped.append(flat[i:i + c])
        
        return reshaped
