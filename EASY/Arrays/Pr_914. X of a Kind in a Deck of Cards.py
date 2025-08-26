from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck):
        # Custom gcd function
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Count frequency of each number
        count = Counter(deck)
        
        # Start gcd with first count
        g = 0
        for c in count.values():
            g = gcd(g, c)
        
        # Partition possible if gcd > 1
        return g > 1
