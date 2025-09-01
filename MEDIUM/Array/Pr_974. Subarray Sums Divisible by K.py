class Solution:
    def subarraysDivByK(self, nums, k):
        count = {0: 1}   # remainder -> frequency, initially remainder 0 seen once
        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            remainder = prefix % k
            
            # Python handles negative modulo differently; normalize
            if remainder < 0:
                remainder += k

            if remainder in count:
                result += count[remainder]  # add all previous matches
                count[remainder] += 1
            else:
                count[remainder] = 1
        
        return result


# Example usage
sol = Solution()
print(sol.subarraysDivByK([4,5,0,-2,-3,1], 5))  # 7
print(sol.subarraysDivByK([5], 9))              # 0
