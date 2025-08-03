class Solution:
    def findRelativeRanks(self, score):
        n = len(score)
        # Step 1: Pair scores with their original indices
        indexed_scores = [(s, i) for i, s in enumerate(score)]
        
        # Step 2: Sort by score in descending order
        indexed_scores.sort(reverse=True)
        
        # Step 3: Prepare the result array
        res = [""] * n
        for rank, (s, i) in enumerate(indexed_scores):
            if rank == 0:
                res[i] = "Gold Medal"
            elif rank == 1:
                res[i] = "Silver Medal"
            elif rank == 2:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank + 1)
        
        return res
