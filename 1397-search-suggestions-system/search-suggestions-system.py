from dataclasses import dataclass

@dataclass
class TreeNode:
    children: Dict[str, "TreeNode"]
    value: str
    isTerminal: bool

    def __str__(self):
        return f"[{self.value}]({self.isTerminal}) - {list(self.children.values())}"

class Trie:
    def __init__(self):
        self.__root = TreeNode({}, '', False)
        self.__threeSmallests = {}
    
    def insert(self, word: str):
        curr = self.__root
        for i, char in enumerate(word):
            if char not in curr.children:
                curr.children[char] = TreeNode({}, char, i == len(word)-1)
            elif i == len(word)-1:
                curr.children[char].isTerminal = True
            curr = curr.children[char]
    
    def __findAll(self, node: "TreeNode", curr: str):
        result = []
        if node.isTerminal:
            result.extend([curr])
        for char in sorted(node.children.keys()):
            result.extend(self.__findAll(node.children[char], curr+char))
        return result
    
    def __findThreeSmallest(self, node: "TreeNode", curr: str):
        result = []
        if node.isTerminal:
            result.extend([curr])
        for char in sorted(node.children.keys()):
            smallests = self.__findThreeSmallest(node.children[char], curr+char)
            if len(result) <= 3:
                result.extend(smallests)
        result = result[:min(3, len(result))]
        self.__threeSmallests[curr] = result
        return result
    
    
    def searchByCharacter(self, searchWord: str) -> List[List[str]]:
        self.__findThreeSmallest(self.__root, "")
        print(self.__threeSmallests)
        result = []
        foundEmpty = False
        currStr = ""
        curr = self.__root
        for i, char in enumerate(searchWord):
            currStr += char
            if foundEmpty or char not in curr.children:
                result.append([])
                foundEmpty = True
            else:
                result.append(self.__threeSmallests[currStr])
                curr = curr.children[char]
        return result
        # result = []
        # foundEmpty = False
        # for i, char in enumerate(searchWord):
        #     if foundEmpty or char not in curr.children:
        #         result.append([])
        #         foundEmpty = True
        #     else:
        #         words = self.__findAll(curr.children[char], searchWord[:i+1])
        #         result.append(words if len(words) <= 3 else words[:3])
        #         curr = curr.children[char]
        # return result
    
    def __repr__(self):
        return str(self.__root)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        return trie.searchByCharacter(searchWord)
