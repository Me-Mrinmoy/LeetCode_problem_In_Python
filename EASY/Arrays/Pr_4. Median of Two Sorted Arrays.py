class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure that nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2

        left, right = 0, m

        while left <= right:
            # Partition in nums1
            i = (left + right) // 2
            # Partition in nums2
            j = half_len - i
            
            # Check if i is perfect
            if i < m and nums1[i] < nums2[j-1]:
                left = i + 1  # i is too small, must increase it
            elif i > 0 and nums1[i-1] > nums2[j]:
                right = i - 1  # i is too big, must decrease it
            else:
                # i is perfect

                # Max of left part
                if i == 0: left_max = nums2[j-1]
                elif j == 0: left_max = nums1[i-1]
                else: left_max = max(nums1[i-1], nums2[j-1])

                # If odd total length, return the max of the left half
                if total_len % 2 == 1:
                    return left_max

                # Min of right part
                if i == m: right_min = nums2[j]
                elif j == n: right_min = nums1[i]
                else: right_min = min(nums1[i], nums2[j])

                # If even total length, return the average of the two middle numbers
                return (left_max + right_min) / 2.0

# Example usage:
nums1 = [1, 3]
nums2 = [2]

solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0
