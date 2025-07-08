class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._peeked = self.iterator.next() if self.iterator.hasNext() else None
        self._has_peeked = self._peeked is not None

    def peek(self):
        return self._peeked

    def next(self):
        current = self._peeked
        self._peeked = self.iterator.next() if self.iterator.hasNext() else None
        self._has_peeked = self._peeked is not None
        return current

    def hasNext(self):
        return self._has_peeked
