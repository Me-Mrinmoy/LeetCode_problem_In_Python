class SnapshotArray:
    def __init__(self, length: int):
        self.cache = []
        self.d = dict()
        self.i = 0

    def set(self, index: int, val: int) -> None:
        self.d[index] = val

    def snap(self) -> int:
        self.cache.append(dict(self.d))
        self.i += 1
        return self.i-1

    def get(self, index: int, snap_id: int) -> int:
        snap = self.cache[snap_id]
        return snap[index] if index in snap else 0
