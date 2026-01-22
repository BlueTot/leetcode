class Node:
    def __init__(self, key, is_final):
        self.key = key
        self.is_final = is_final
        self.nexts = {}


class WordDictionary:

    def __init__(self):
        self.__root = Node('', False)
        

    def addWord(self, word: str) -> None:

        curr = self.__root

        for char in word:

            # if we have a child to go to
            if char in curr.nexts:
                curr = curr.nexts[char]
            
            # no child, we must create it
            else:
                curr.nexts[char] = Node(char, False)
                curr = curr.nexts[char]
        
        # at the end, we insert the word
        curr.is_final = True
    
    def __search(self, curr: Node, word: str, index: int) -> bool:

        if index == len(word):
            return curr.is_final

        # wildcard
        if word[index] == '.':
            for child in curr.nexts:
                if self.__search(curr.nexts[child], word, index + 1):
                    return True
            return False
        
        # character
        else:
            if word[index] not in curr.nexts:
                return False
            return self.__search(curr.nexts[word[index]], word, index + 1)


    def search(self, word: str) -> bool:
        return self.__search(self.__root, word, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)