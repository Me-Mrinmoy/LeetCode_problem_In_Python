class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and a < 0:
                top = stack[-1]
                if top < -a:          # top explodes; keep checking
                    stack.pop()
                elif top == -a:       # both explode
                    stack.pop()
                    alive = False
                else:                 # top is bigger; current explodes
                    alive = False
            if alive:
                stack.append(a)
        return stack
