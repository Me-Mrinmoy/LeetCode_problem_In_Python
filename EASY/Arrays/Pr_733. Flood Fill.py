class Solution:
    def floodFill(self, image, sr, sc, newColor):
        # iterative DFS to avoid recursion depth issues
        original = image[sr][sc]
        if original == newColor:
            return image

        m = len(image)
        n = len(image[0])
        stack = [(sr, sc)]

        while stack:
            r, c = stack.pop()
            if image[r][c] != original:
                continue
            image[r][c] = newColor
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original:
                    stack.append((nr, nc))

        return image


if __name__ == "__main__":
    img = [
        [1,1,1],
        [1,1,0],
        [1,0,1]
    ]
    # flood fill starting at (1,1) changing color to 2
    out = Solution().floodFill(img, 1, 1, 2)
    print(out)  # expected: [[2,2,2],[2,2,0],[2,0,1]]
