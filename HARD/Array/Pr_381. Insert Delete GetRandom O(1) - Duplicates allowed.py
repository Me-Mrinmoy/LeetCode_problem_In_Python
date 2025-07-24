import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.nums = []  # list of all values (with duplicates)
        self.idx_map = defaultdict(set)  # val -> set of indices in nums

    def insert(self, val):
        self.nums.append(val)
        self.idx_map[val].add(len(self.nums) - 1)
        return len(self.idx_map[val]) == 1  # True if it was the first occurrence

    def remove(self, val):
        if not self.idx_map[val]:
            return False

        remove_idx = self.idx_map[val].pop()  # get any index of val
        last_val = self.nums[-1]

        # Replace remove_idx with last_val if not same
        if remove_idx != len(self.nums) - 1:
            self.nums[remove_idx] = last_val
            self.idx_map[last_val].add(remove_idx)
            self.idx_map[last_val].discard(len(self.nums) - 1)

        self.nums.pop()

        # Clean up if val no longer exists
        if not self.idx_map[val]:
            del self.idx_map[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)
