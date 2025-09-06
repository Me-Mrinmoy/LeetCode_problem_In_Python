class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        sm=float('inf')
        for i in range(len(nums)):
            sm=min(sm,abs(nums[i]))
            if nums[i]<0 and k>0:
                nums[i]=-1*nums[i]
                k-=1
        if k%2==1:
            return sum(nums)-(2*sm)
        return sum(nums)
        

            
        
