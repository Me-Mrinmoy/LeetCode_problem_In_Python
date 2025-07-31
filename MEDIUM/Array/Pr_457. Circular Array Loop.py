class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)
        
        def next_index(i):
            return (i + nums[i]) % n
        
        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i
            direction = nums[i] > 0  # True for positive, False for negative

            while True:
                # Move slow once
                next_slow = next_index(slow)
                # Move fast twice
                next_fast = next_index(fast)
                if nums[next_fast] * nums[fast] <= 0 or nums[next_slow] * nums[slow] <= 0:
                    break
                next_fast = next_index(next_fast)
                if nums[next_fast] * nums[fast] <= 0:
                    break

                if next_slow == next_fast:
                    if next_slow == next_index(next_slow):  # single element loop
                        break
                    return True

                slow, fast = next_slow, next_fast

            # Mark all elements in this path as 0 to avoid revisiting
            j = i
            sign = nums[i]
            while nums[j] * sign > 0:
                next_j = next_index(j)
                nums[j] = 0
                j = next_j

        return False
