class Solution:
    def numSpecialEquivGroups(self, words):
        signatures = set()
        
        for word in words:
            even_chars = sorted(word[0::2])  # chars at even indices
            odd_chars = sorted(word[1::2])   # chars at odd indices
            signatures.add(("".join(even_chars), "".join(odd_chars)))
        
        return len(signatures)


# Example usage:
solution = Solution()
print(solution.numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))  # Output: 3
print(solution.numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))        # Output: 3
