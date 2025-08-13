class WordFilter:
    def __init__(self, words):
        self.lookup = {}
        for i, word in enumerate(words):
            n = len(word)
            for p in range(n + 1):  # prefix length
                prefix = word[:p]
                for s in range(n + 1):  # suffix length
                    suffix = word[n - s:]
                    self.lookup[(prefix, suffix)] = i  # overwrite with latest index

    def f(self, pref, suff):
        return self.lookup.get((pref, suff), -1)
