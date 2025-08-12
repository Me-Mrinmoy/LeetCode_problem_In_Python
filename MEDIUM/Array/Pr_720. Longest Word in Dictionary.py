class Solution:
    def longestWord(self, words):
        # sort by length then lexicographically
        words.sort(key=lambda x: (len(x), x))

        built = set([""])
        longest = ""

        for w in words:
            if w[:-1] in built:
                built.add(w)
                if len(w) > len(longest) or (len(w) == len(longest) and w < longest):
                    longest = w
        return longest

# quick test
if __name__ == "__main__":
    print(Solution().longestWord(["w","wo","wor","worl","world"]))  # world
    print(Solution().longestWord(["a","banana","app","appl","ap","apply","apple"]))  # apple
