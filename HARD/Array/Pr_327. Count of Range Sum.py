class Solution:
    def countRangeSum(self, nums, lower, upper):
        def merge_sort(start, end):
            if end - start <= 1:
                return 0
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid, end)
            j = k = mid
            for left in prefix[start:mid]:
                while k < end and prefix[k] - left < lower:
                    k += 1
                while j < end and prefix[j] - left <= upper:
                    j += 1
                count += j - k
            prefix[start:end] = sorted(prefix[start:end])
            return count

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        return merge_sort(0, len(prefix))
