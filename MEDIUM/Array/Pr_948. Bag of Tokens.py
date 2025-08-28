class Solution:
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        lo, hi = 0, len(tokens) - 1
        score = max_score = 0

        while lo <= hi:
            if power >= tokens[lo]:
                power -= tokens[lo]
                score += 1
                lo += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[hi]
                score -= 1
                hi -= 1
            else:
                break

        return max_score
