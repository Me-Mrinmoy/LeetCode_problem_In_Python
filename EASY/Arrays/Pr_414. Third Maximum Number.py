class Solution:
    def thirdMax(self, nums):
        distinct = list(set(nums))  # Remove duplicates
        distinct.sort(reverse=True)  # Sort in descending order

        if len(distinct) >= 3:
            return distinct[2]  # 3rd maximum
        else:
            return distinct[0]  # Return max
