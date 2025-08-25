class RLEIterator:
    def __init__(self, encoding):
        self.encoding = encoding
        self.i = 0  # pointer to counts (even index)

    def next(self, n):
        while self.i < len(self.encoding) and n > 0:
            if self.encoding[self.i] >= n:
                # consume from this run
                self.encoding[self.i] -= n
                return self.encoding[self.i + 1]
            else:
                # skip entire run
                n -= self.encoding[self.i]
                self.i += 2
        return -1
