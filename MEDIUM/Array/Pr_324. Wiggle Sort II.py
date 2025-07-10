class Solution(object):
    def wiggleSort(self, nums):
        import random

        def find_kth_largest(k):
            def partition(left, right, pivot_index):
                pivot = nums[pivot_index]
                nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
                store_index = left
                for i in range(left, right):
                    if nums[i] < pivot:
                        nums[store_index], nums[i] = nums[i], nums[store_index]
                        store_index += 1
                nums[right], nums[store_index] = nums[store_index], nums[right]
                return store_index

            left, right = 0, len(nums) - 1
            while True:
                pivot_index = random.randint(left, right)
                pos = partition(left, right, pivot_index)
                if pos == k:
                    return nums[pos]
                elif pos < k:
                    left = pos + 1
                else:
                    right = pos - 1

        n = len(nums)
        median = find_kth_largest((n - 1) // 2)

        # Virtual index mapping
        def index(i):
            return (1 + 2 * i) % (n | 1)

        # 3-way partition (Dutch National Flag)
        left, i, right = 0, 0, n - 1
        while i <= right:
            if nums[index(i)] > median:
                nums[index(left)], nums[index(i)] = nums[index(i)], nums[index(left)]
                left += 1
                i += 1
            elif nums[index(i)] < median:
                nums[index(right)], nums[index(i)] = nums[index(i)], nums[index(right)]
                right -= 1
            else:
                i += 1
