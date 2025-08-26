class Solution:
    def sortArray(self, nums):
        n = len(nums)
        
        # Heapify function (max heap)
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            # Check if left child exists and is greater
            if left < n and arr[left] > arr[largest]:
                largest = left
                
            # Check if right child exists and is greater
            if right < n and arr[right] > arr[largest]:
                largest = right
                
            # If root is not largest, swap and continue heapifying
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        # Step 1: Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)
        
        # Step 2: Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # swap root with last element
            heapify(nums, i, 0)  # heapify reduced heap
        
        return nums
