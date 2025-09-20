class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0

        for i in words:
            for j in i:
                if i.count(j) > chars.count(j):
                    break
            else:
                res += len(i)
        return res
