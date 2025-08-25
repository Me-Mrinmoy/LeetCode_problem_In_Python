class Solution:
    def totalFruit(self, fruits):
        left = 0
        count = {}
        max_len = 0

        for right, f in enumerate(fruits):
            count[f] = count.get(f, 0) + 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
