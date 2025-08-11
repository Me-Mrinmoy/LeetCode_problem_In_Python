class MyHashMap:

    def __init__(self):
        self.size = 1000  # number of buckets
        self.buckets = [[] for _ in range(self.size)]
        
    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[h]):
            if k == key:
                self.buckets[h][i] = (key, value)  # update existing
                return
        self.buckets[h].append((key, value))  # insert new

    def get(self, key):
        h = self._hash(key)
        for (k, v) in self.buckets[h]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[h]):
            if k == key:
                self.buckets[h].pop(i)
                return
