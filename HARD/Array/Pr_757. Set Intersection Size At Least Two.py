class Solution:
    def intersectionSizeTwo(self, intervals):
        # Step 1: sort by end ascending, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # The two largest picked numbers so far
        p1 = p2 = -1
        result = 0
        
        for start, end in intervals:
            # Case 1: Both are outside the interval
            if p2 < start:
                result += 2
                p1 = end - 1
                p2 = end
            # Case 2: Only p2 is in range
            elif p1 < start:
                result += 1
                p1 = p2
                p2 = end
            # Case 3: Both inside -> do nothing
        
        return result


# Example runs
print(Solution().intersectionSizeTwo([[1,3],[3,7],[8,9]]))  # 5
print(Solution().intersectionSizeTwo([[1,3],[1,4],[2,5],[3,5]]))  # 3
print(Solution().intersectionSizeTwo([[1,2],[2,3],[2,4],[4,5]]))  # 5
