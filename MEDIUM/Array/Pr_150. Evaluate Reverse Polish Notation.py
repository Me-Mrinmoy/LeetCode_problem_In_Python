class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                result = 0
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    result = int(float(a) / b)  # use float for division then convert to int
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]

# Example usage
tokens = ["2", "1", "+", "3", "*"]
solution = Solution()
print(solution.evalRPN(tokens))  # Output should be 9
