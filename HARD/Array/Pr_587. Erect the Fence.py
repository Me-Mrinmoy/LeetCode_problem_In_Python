class Solution:
    def outerTrees(self, trees):
        trees.sort()

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        lower = []
        for tree in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], tree) < 0:
                lower.pop()
            lower.append(tuple(tree))

        upper = []
        for tree in reversed(trees):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], tree) < 0:
                upper.pop()
            upper.append(tuple(tree))

        return list(set(lower + upper))
