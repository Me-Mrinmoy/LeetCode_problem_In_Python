class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        shift_count = {}
        max_overlap = 0

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                shift = (x2 - x1, y2 - y1)
                shift_count[shift] = shift_count.get(shift, 0) + 1
                max_overlap = max(max_overlap, shift_count[shift])

        return max_overlap
