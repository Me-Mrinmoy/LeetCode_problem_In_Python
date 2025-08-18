class Solution:
    def numComponents(self, head, nums):
        nums_set = set(nums)
        count = 0
        in_component = False

        curr = head
        while curr:
            if curr.val in nums_set:
                if not in_component:
                    count += 1   # start of a new component
                    in_component = True
            else:
                in_component = False  # ended component
            curr = curr.next

        return count
