def maxSumOfThreeSubarrays(nums, k):
    n = len(nums)
    if n < 3 * k:
        return []

    # sums of each k-length window
    window_sum = [0] * (n - k + 1)
    cur = sum(nums[:k])
    window_sum[0] = cur
    for i in range(1, n - k + 1):
        cur += nums[i + k - 1] - nums[i - 1]
        window_sum[i] = cur

    m = len(window_sum)

    # best left index for every position
    left = [0] * m
    best = 0
    for i in range(m):
        if window_sum[i] > window_sum[best]:
            best = i
        left[i] = best

    # best right index for every position
    right = [0] * m
    best = m - 1
    for i in range(m - 1, -1, -1):
        if window_sum[i] >= window_sum[best]:
            best = i
        right[i] = best

    # try every middle window
    max_total = -1
    ans = [0, 0, 0]
    for mid in range(k, m - k):
        l = left[mid - k]
        r = right[mid + k]
        total = window_sum[l] + window_sum[mid] + window_sum[r]
        if total > max_total:
            max_total = total
            ans = [l, mid, r]

    return ans

# quick tests
print(maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))   # [0, 3, 5]
print(maxSumOfThreeSubarrays([1,2,1,2,1,2,1,2,1], 2)) # [0, 2, 4]
