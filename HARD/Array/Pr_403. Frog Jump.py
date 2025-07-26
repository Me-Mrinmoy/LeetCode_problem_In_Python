class Solution:
    def canCross(self, stones):
        stone_set = set(stones)
        last_stone = stones[-1]
        memo = {}

        def dfs(position, jump):
            if (position, jump) in memo:
                return memo[(position, jump)]

            if position == last_stone:
                return True

            for next_jump in [jump - 1, jump, jump + 1]:
                if next_jump > 0:
                    next_pos = position + next_jump
                    if next_pos in stone_set:
                        if dfs(next_pos, next_jump):
                            memo[(position, jump)] = True
                            return True

            memo[(position, jump)] = False
            return False

        # The first jump must be exactly 1 unit
        return dfs(1, 1) if 1 in stone_set else False
