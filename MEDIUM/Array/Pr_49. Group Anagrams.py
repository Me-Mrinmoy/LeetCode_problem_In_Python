from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Dictionary to hold groups of anagrams
        anagrams = defaultdict(list)
        
        for s in strs:
            # Sort the string to get the key
            sorted_str = ''.join(sorted(s))
            # Append the original string to the list corresponding to the sorted key
            anagrams[sorted_str].append(s)
        
        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())

# Example usage
solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs))  # Output: [["eat", "tea", "ate"], ["nat", "tan"], ["bat"]]
