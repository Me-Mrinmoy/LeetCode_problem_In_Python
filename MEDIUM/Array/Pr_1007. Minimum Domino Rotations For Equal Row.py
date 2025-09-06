class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        def check(target):
            top_swaps = bottom_swaps = 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return float('inf')  
                elif tops[i] != target:
                    top_swaps += 1 
                elif bottoms[i] != target:
                    bottom_swaps += 1  
            return min(top_swaps, bottom_swaps) 
        
        rotations = min(check(tops[0]), check(bottoms[0]))
        return rotations if rotations != float('inf') else -1
