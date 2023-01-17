class TrieNode:

    def __init__(self):
        self.__nodes = dict()
        self.__terminates_word = False
        self.__value = None

    def add_word(self, word):
        if len(word) < 1:
            raise Exception("Empty word supplied")
        if word[0:1] not in self.__nodes:
            self.__nodes[word[0:1]] = TrieNode()
        if len(word) > 1:
            self.__nodes[word[0:1]].add_word(word[1:])
        else:
            self.__nodes[word[0:1]].terminates_word = True

    def contains_word(self, word):
        if len(word) == 1:
            return word in self.__nodes and self.__nodes[word].terminates_word
        else:
            return word[0:1] in self.__nodes and self.__nodes[word[0:1]].contains_word(word[1:])

    @property
    def terminates_word(self):
        return self.__terminates_word

    @terminates_word.setter
    def terminates_word(self, value):
        self.__terminates_word = value

    @property
    def size(self):
        words_here = 0
        if self.__terminates_word:
            words_here = 1
        for n in self.__nodes:
            words_here = words_here + self.__nodes[n].size
        return words_here




