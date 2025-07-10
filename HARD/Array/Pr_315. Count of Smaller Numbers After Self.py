class Solution(object):
    def countSmaller(self, nums):
        n = len(nums)
        counts = [0] * n
        indexes = list(range(n))  # store original indexes

        def merge_sort(start, end):
            if end - start <= 1:
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)
            merge(start, mid, end)

        def merge(start, mid, end):
            temp = []
            i, j = start, mid
            right_count = 0

            while i < mid and j < end:
                if nums[indexes[j]] < nums[indexes[i]]:
                    temp.append(indexes[j])
                    right_count += 1
                    j += 1
                else:
                    temp.append(indexes[i])
                    counts[indexes[i]] += right_count
                    i += 1

            while i < mid:
                temp.append(indexes[i])
                counts[indexes[i]] += right_count
                i += 1

            while j < end:
                temp.append(indexes[j])
                j += 1

            # write back to indexes
            for i in range(len(temp)):
                indexes[start + i] = temp[i]

        merge_sort(0, n)
        return counts
