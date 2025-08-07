def replaceWords(dictionary, sentence):
    root_set = set(dictionary)

    def find_root(word):
        for i in range(1, len(word) + 1):
            if word[:i] in root_set:
                return word[:i]
        return word

    words = sentence.split()
    replaced = [find_root(word) for word in words]
    return ' '.join(replaced)

# Example usage
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(replaceWords(dictionary, sentence))
