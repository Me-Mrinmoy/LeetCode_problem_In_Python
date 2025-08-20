class Solution:
    def longestMountain(self, arr):
        n = len(arr)
        ans = 0
        i = 1  # start from 1 because first can't be peak
        
        while i < n - 1:
            # check if arr[i] is a peak
            if arr[i-1] < arr[i] > arr[i+1]:
                left = i - 1
                right = i + 1
                
                # expand left
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1
                
                # expand right
                while right < n-1 and arr[right] > arr[right+1]:
                    right += 1
                
                ans = max(ans, right - left + 1)
                i = right  # jump to end of this mountain
            else:
                i += 1
        
        return ans
