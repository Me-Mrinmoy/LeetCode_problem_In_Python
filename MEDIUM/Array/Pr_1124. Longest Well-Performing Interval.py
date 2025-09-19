class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        ans = diff = 0                              # diff tracks tire-days-not-tire-days
        pref = defaultdict(int)                     # acts like a prefix array

        for i,hour in enumerate(hours):
            if diff not in pref: pref[diff] = i     # add key to dict
 
            diff+= 2*(hour > 8) - 1                 # +1 for tire-day,  -1 for not-tire-day 
                                                    
            if diff-1 in pref:
                ans = max(ans,              
                          i+1-pref[diff-1],         # num[pref[diff-1]:i+1] is "well-performing"
                          i+1 if diff > 0 else 0)   # num[:i+1] is "well-performing" if diff > 0.
                      
        return ans   
