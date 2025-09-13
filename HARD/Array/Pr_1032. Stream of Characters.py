from collections import deque

class StreamChecker:

    def __init__(self, words: list[str]):
        # 1)reversed trie
        self.trie = {}  # root node; each node is a dict: { 'is_word': bool, 'children': {char: node} }
        self.max_len = 0

        for w in words:
            self.max_len = max(self.max_len, len(w))
            node = self.trie
            for ch in reversed(w):
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            # Mark word end (world end lol)
            node['~'] = True  # '~' sentinel to indicate complete words
        self.buffer = deque(maxlen=self.max_len)

    def query(self, letter: str) -> bool:
        self.buffer.appendleft(letter)
        node = self.trie
        for ch in self.buffer:
            if ch not in node:
                return False
            node = node[ch]
            # If hit a node '~': matchfull reversed word
            if '~' in node:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
