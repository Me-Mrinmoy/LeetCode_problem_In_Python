class Solution:
    def spellchecker(self, wordlist, queries):
        wordset = set(wordlist)
        cap_map = {}
        vowel_map = {}

        def devowel(word):
            return ''.join('*' if c.lower() in "aeiou" else c.lower() for c in word)

        for word in wordlist:
            lower_word = word.lower()
            cap_map.setdefault(lower_word, word)
            vowel_map.setdefault(devowel(lower_word), word)

        ans = []
        for query in queries:
            if query in wordset:
                ans.append(query)
            elif query.lower() in cap_map:
                ans.append(cap_map[query.lower()])
            elif devowel(query.lower()) in vowel_map:
                ans.append(vowel_map[devowel(query.lower())])
            else:
                ans.append("")
        return ans
