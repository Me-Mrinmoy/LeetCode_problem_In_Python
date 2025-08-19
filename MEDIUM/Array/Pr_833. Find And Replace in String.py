class Solution:
    def findReplaceString(self, s, indices, sources, targets):
        replacements = sorted(zip(indices, sources, targets), reverse=True)
        
        for i, src, tgt in replacements:
            if s[i:i+len(src)] == src:
                s = s[:i] + tgt + s[i+len(src):]
        
        return s
