class Solution:
    def tallestBillboard(self, rods):
        # dp[diff] = max height of the shorter support with (left - right) = diff
        dp = {0: 0}
        for r in rods:
            new_dp = dict(dp)           # copy so we iterate over previous state
            for diff, short in dp.items():
                # put rod on left -> diff increases, short stays same
                nd = diff + r
                if new_dp.get(nd, -1) < short:
                    new_dp[nd] = short

                # put rod on right -> diff becomes abs(diff - r)
                # shorter side increases by min(r, diff)
                nd = abs(diff - r)
                added = short + min(r, diff)
                if new_dp.get(nd, -1) < added:
                    new_dp[nd] = added

            dp = new_dp
        return dp.get(0, 0)
