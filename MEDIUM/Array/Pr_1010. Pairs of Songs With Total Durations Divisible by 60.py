class Solution(object):
    def numPairsDivisibleBy60(self, time):
        ans, cnt = 0, [0] * 60
        for t in time: cnt[t % 60] += 1
        for i in range(1, 30): ans += cnt[i] * cnt[60 - i]
        return ans + cnt[0] * (cnt[0] - 1) // 2 + cnt[30] * (cnt[30] - 1) // 2
