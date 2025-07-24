import random

class RandomizedSet:

    def __init__(self):
        self.num_to_index = {}  # maps value -> index in list
        self.nums = []          # stores values

    def insert(self, val):
        if val in self.num_to_index:
            return False
        self.nums.append(val)
        self.num_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        if val not in self.num_to_index:
            return False

        index = self.num_to_index[val]
        last_val = self.nums[-1]

        # Swap val with the last element
        self.nums[index] = last_val
        self.num_to_index[last_val] = index

        # Remove val
        self.nums.pop()
        del self.num_to_index[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)
