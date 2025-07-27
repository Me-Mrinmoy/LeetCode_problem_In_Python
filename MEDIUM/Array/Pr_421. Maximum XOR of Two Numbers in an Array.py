class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def findMaximumXOR(self, nums):
        root = TrieNode()
        
        # Insert a number into Trie (bit by bit)
        def insert(num):
            node = root
            for i in range(31, -1, -1):  # 32 bits for integers up to 2^31
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        # Find best XOR for this number from existing Trie
        def findMaxXOR(num):
            node = root
            max_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                # We want the opposite bit to maximize XOR
                toggled_bit = 1 - bit
                if toggled_bit in node.children:
                    max_xor |= (1 << i)
                    node = node.children[toggled_bit]
                else:
                    node = node.children.get(bit, node)
            return max_xor

        max_result = 0
        insert(nums[0])  # Insert first number

        for i in range(1, len(nums)):
            max_result = max(max_result, findMaxXOR(nums[i]))
            insert(nums[i])

        return max_result
