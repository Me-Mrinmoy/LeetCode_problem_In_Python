class Solution:
    def flipAndInvertImage(self, image):
        for row in image:
            row.reverse()
            for j in range(len(row)):
                row[j] ^= 1
        return image
