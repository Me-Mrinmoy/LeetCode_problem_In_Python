from bisect import bisect_right

class TopVotedCandidate:
    def __init__(self, persons, times):
        self.times = times
        self.leaders = []
        counts = {}
        leader = -1
        max_votes = 0

        for p in persons:
            counts[p] = counts.get(p, 0) + 1
            # tie goes to the most recent vote: use >=
            if counts[p] >= max_votes:
                leader = p
                max_votes = counts[p]
            self.leaders.append(leader)

    def q(self, t):
        # latest time <= t
        idx = bisect_right(self.times, t) - 1
        return self.leaders[idx]
