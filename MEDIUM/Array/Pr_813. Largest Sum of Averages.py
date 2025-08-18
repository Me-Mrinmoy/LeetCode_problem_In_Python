class Solution:
    def largestSumOfAverages(self, nums, k):
        n = len(nums)

        # prefix sums as floats for safe division
        prefix = [0.0]
        s = 0.0
        for x in nums:
            s += float(x)
            prefix.append(s)

        # dp[i] = best score for first i elements with current number of groups
        dp = [0.0] * (n + 1)
        # base: 1 group -> average of first i elements
        for i in range(1, n + 1):
            dp[i] = (prefix[i] - prefix[0]) / float(i)

        # add groups 2..k
        for groups in range(2, k + 1):
            new_dp = [0.0] * (n + 1)
            # need at least `groups` elements to form `groups` non-empty parts
            for i in range(groups, n + 1):
                best = 0.0
                # last group starts at m (size at least 1): m in [groups-1, i-1]
                for m in range(groups - 1, i):
                    avg_last = (prefix[i] - prefix[m]) / float(i - m)
                    cand = dp[m] + avg_last
                    if cand > best:
                        best = cand
                new_dp[i] = best
            dp = new_dp

        return dp[n]
