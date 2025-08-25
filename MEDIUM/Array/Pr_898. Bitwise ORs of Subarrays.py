class Solution:
    def subarrayBitwiseORs(self, arr):
        res = set()
        prev = set()
        
        for num in arr:
            # New set of ORs for subarrays ending at this element
            curr = {num}
            for val in prev:
                curr.add(val | num)
            
            res |= curr     # add to global results
            prev = curr     # move to next step
        
        return len(res)
