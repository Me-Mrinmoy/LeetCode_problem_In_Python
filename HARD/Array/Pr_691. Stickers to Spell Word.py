# LeetCode-style class: Python 2 & 3 compatible, no lru_cache
class Solution:
    def minStickers(self, stickers, target):
        # build count arrays for stickers
        sticker_counts = []
        for s in stickers:
            cnt = [0]*26
            for ch in s:
                cnt[ord(ch)-97] += 1
            sticker_counts.append(tuple(cnt))

        # target count
        target_count = [0]*26
        for ch in target:
            target_count[ord(ch)-97] += 1
        target_key = tuple(target_count)

        # filter stickers that have no useful chars for target
        useful = []
        for sc in sticker_counts:
            ok = False
            for i in range(26):
                if sc[i] > 0 and target_count[i] > 0:
                    ok = True
                    break
            if ok:
                useful.append(list(sc))  # keep as list for comparisons

        if not useful:
            return -1

        # remove dominated stickers: if sticker A is dominated by B (B has >= counts for all letters),
        # then A can be removed
        filtered = []
        for i, si in enumerate(useful):
            dominated = False
            for j, sj in enumerate(useful):
                if i != j:
                    # if sj >= si for all letters, sj dominates si
                    if all(sj[x] >= si[x] for x in range(26)):
                        # if equal vectors, keep only one (by index tie-break)
                        if sj != si or j < i:
                            dominated = True
                            break
            if not dominated:
                filtered.append(tuple(si))

        sticker_counts = filtered

        memo = { (0,)*26: 0 }

        def dfs(key):
            if key in memo:
                return memo[key]

            # pick pivot letter = index with largest remaining count (heuristic)
            pivot = max(range(26), key=lambda x: key[x])
            if key[pivot] == 0:
                memo[key] = 0
                return 0

            best = float('inf')
            for sc in sticker_counts:
                if sc[pivot] == 0:
                    continue
                # apply sticker sc once and compute remaining key
                nxt = []
                for i in range(26):
                    rem = key[i] - sc[i]
                    nxt.append(rem if rem > 0 else 0)
                nxt = tuple(nxt)
                res = dfs(nxt)
                if res != -1:
                    best = min(best, 1 + res)

            memo[key] = -1 if best == float('inf') else best
            return memo[key]

        return dfs(target_key)


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.minStickers(["with","example","science"], "thehat"))   # -> 3
    print(sol.minStickers(["notice","possible"], "basicbasic"))     # -> -1
