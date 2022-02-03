
"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.

"""


from collections import defaultdict


class TrieNode:
    def __init__(self, val:str):
        self.val = val
        self.children = {}
        self.isword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode('*')
        

    def addWord(self, word: str) -> None:
        head = self.root
        for c in word:
            if c not in head.children:
                head.children[c] = TrieNode(c)
            head = head.children[c]
        head.isword = True        

    def search(self, word: str) -> bool:
        
        def dfs(head: TrieNode,word:str)-> bool:
            for i ,c in enumerate(word):
                if c == '.':
                    for ch in head.children:
                        if dfs(head.children[ch], word[i+1:]): 
                            return True
                    return False
                if c not in head.children:
                    return False
                head = head.children[c]
            return head.isword

        return dfs(self.root, word)

    def startsWith(self, word:str) -> bool:
        head = self.root
        for c in word:
            if c not in head.children:
                return False
        return True
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

s= WordDictionary()

s.addWord('bad')
s.addWord('dad')
s.addWord('mad')
s.addWord('shop')
s.addWord('shoping')
s.addWord('shopper')
print(s.search('sh.'))
print(s.startsWith('sh'))
print(s.search('mad'))
print(s.search('.ad'))
print(s.search('bbd'))
print(s.search('.bd'))
print(s.search('..d'))