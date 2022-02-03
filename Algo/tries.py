class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.Node = TrieNode('*')

    def insert(self, word):
        head = self.Node
        for chr in word:
            if chr not in head.children:
                head.children[chr] = TrieNode(chr)
            head = head.children[chr]
        head.isWord = True

    def search(self, word):
        head = self.Node
        for chr in word:
            if chr not in head.children:
                return False
            head = head.children[chr]
        return head.isWord

    def startsWith(self, word):
        head = self.Node
        for chr in word:
            if chr not in head.children:
                return False
            head = head.children[chr] 
        return True

class Trie2:
    def __init__(self):
        self.root = {'*':'*'}

    def insert(self, word):
        head = self.root
        for ch in word:
            if ch not in head:
                head[ch] = {}
            head = head[ch]
        head[ch] = '*'

    def printdict(self):
        for k,v in self.root.items():
            print(f'{k}: {v}')


    def search(self, word):
        head = self.root
        for ch in word:
            if ch not in head:
                return False
            head = head[ch]
        return '*' in head

s = Trie()

s.insert('shop') 
s.insert('shpper')
s.insert('bank')
s.insert('banker')

print(s.search('shop'))  #true
print(s.startsWith('sh')) #true
print(s.search('bankrate')) #false
print(s.search('shope')) #false
print(s.startsWith('bb')) #false

s1 =Trie2()

s1.insert('shop')

s1.insert('shoper')

s1.insert('wait')

s1.insert('waiting')

s1.insert('bad')
s1.insert('mad')
s1.insert('dad')

s1.printdict()