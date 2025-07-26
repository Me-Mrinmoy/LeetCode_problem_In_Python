import random

class Solution:
    def __init__(self, nums):
        self.original = nums[:]  # Store the original array
        self.array = nums[:]

    def reset(self):
        self.array = self.original[:]  # Reset to original
        return self.array

    def shuffle(self):
        array = self.array[:]
        n = len(array)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            array[i], array[j] = array[j], array[i]
        return array
