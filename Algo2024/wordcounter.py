class Solution:
    def count(self,word):
        freq = [0]* 26
        for c in word:
            freq[ord(c) - ord('a')] += 1
        return freq
    
    def intersect (self, freq1, freq2):
        return [ min(f1, f2) for f1,f2 in zip(freq1, freq2)]


    def commonChars(self, words: list) -> list:
        first = self.count(words[0])
        for w in words:
            first = self.intersect(first, self.count(w))
        res = []
        for i in range(26):
            res.extend([chr(i + ord('a'))] * first[i])
        return(res)

s =Solution()
print(s.commonChars(['label','bella','roller']))
print(s.commonChars(['toy','joy','boy']))