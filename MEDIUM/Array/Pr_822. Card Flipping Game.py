class Solution:
    def flipgame(self, fronts, backs):
        banned = {f for f, b in zip(fronts, backs) if f == b}
        candidates = set(fronts) | set(backs)
        valid = [x for x in candidates if x not in banned]
        return min(valid) if valid else 0
