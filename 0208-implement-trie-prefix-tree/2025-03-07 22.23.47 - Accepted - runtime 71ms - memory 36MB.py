class Node:
    def __init__(self, char, word):
        self.char = char
        self.word = word
        self.isWord = False
        self.nexts = {}
    def __repr__(self):
        return f"{self.char} {self.isWord} {self.nexts}"

class Trie:

    def __init__(self):
        self.__root = Node("", "")


    def insert(self, word: str) -> None:
        curr = self.__root
        i = 0
        while True:
            if curr.char == word:
                break
            elif curr.word == word:
                curr.char = word
                curr.isWord = True
                break
            elif word[i] in curr.nexts:
                curr = curr.nexts[word[i]]
            else:
                curr.nexts[word[i]] = Node(word[i] if i != len(word)-1 else word, 
                                            word[:i+1])
                if (i == len(word) - 1):
                    curr.nexts[word[i]].isWord = True
                curr = curr.nexts[word[i]]
            i += 1
        #print(self.__root)

    def search(self, word: str) -> bool:
        curr = self.__root
        i = 0
        while i < len(word):
            #print(curr.char, curr.word, i, word)
            if curr.char == word and curr.isWord:
                return True
            elif word[i] in curr.nexts:
                curr = curr.nexts[word[i]]
            else:
                return False
            i += 1
        return curr.char == word and curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.__root
        i = 0
        while i < len(prefix):
            if curr.word == prefix:
                return True
            elif prefix[i] in curr.nexts:
                curr = curr.nexts[prefix[i]]
            else:
                return False
            i += 1
        return curr.word == prefix
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)