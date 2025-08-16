class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        low, high = 0.0, 1.0

        while True:
            mid = (low + high) / 2.0
            count = 0
            i = 0
            best_num, best_den = 0, 1

            for j in range(1, n):
                # Increase i while arr[i]/arr[j] <= mid
                while i < j and arr[i] <= mid * arr[j]:
                    i += 1
                count += i
                if i > 0:
                    # Keep the maximum fraction <= mid
                    if best_num * arr[j] < arr[i - 1] * best_den:
                        best_num, best_den = arr[i - 1], arr[j]

            if count == k:
                return [best_num, best_den]
            elif count < k:
                low = mid
            else:
                high = mid
