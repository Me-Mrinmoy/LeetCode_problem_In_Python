class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {}
        for idx, word in enumerate(list1):
            index_map[word] = idx
        
        min_sum = float('inf')
        result = []

        for idx2, word in enumerate(list2):
            if word in index_map:
                idx1 = index_map[word]
                total = idx1 + idx2
                if total < min_sum:
                    min_sum = total
                    result = [word]
                elif total == min_sum:
                    result.append(word)
        
        return result
