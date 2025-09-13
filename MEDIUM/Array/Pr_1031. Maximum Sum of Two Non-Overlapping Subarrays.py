class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        def getMaxSum(first, second):
            maxFirst, res = 0, 0
            prefix = [0] * (len(nums) + 1)  

            for i in range(len(nums)):
                prefix[i + 1] = prefix[i] + nums[i]

            for i in range(first + second, len(nums) + 1):
                maxFirst = max(maxFirst, prefix[i - second] - prefix[i - first - second])
                res = max(res, maxFirst + prefix[i] - prefix[i - second])
            return res

        return max(getMaxSum(firstLen, secondLen), getMaxSum(secondLen, firstLen))
