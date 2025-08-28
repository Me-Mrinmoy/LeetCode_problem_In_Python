class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0  # pointer for popped
        for x in pushed:
            stack.append(x)
            # keep popping if top matches popped[j]
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack
