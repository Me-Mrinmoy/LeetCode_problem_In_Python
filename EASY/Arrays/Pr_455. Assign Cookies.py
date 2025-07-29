class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        child = 0
        cookie = 0
        
        # Try to satisfy children greedily
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1  # This child is content
            cookie += 1  # Use this cookie whether it's used or skipped
        
        return child

# Example usage:
if __name__ == "__main__":
    sol = Solution()

    print("Output 1:", sol.findContentChildren([1,2,3], [1,1]))  # Output: 1
    print("Output 2:", sol.findContentChildren([1,2], [1,2,3]))  # Output: 2
