import collections
import re

class Solution:
    def mostCommonWord(self, paragraph, banned):
        # normalize: lowercase + replace non-letters with spaces
        words = re.findall(r'\w+', paragraph.lower())
        
        banned_set = set(banned)
        
        count = collections.Counter(word for word in words if word not in banned_set)
        
        # return word with max frequency
        return max(count, key=count.get)
