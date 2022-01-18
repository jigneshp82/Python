import re


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        stringlist = s.split(' ')

        if len(stringlist) != len(pattern):
            return False

        l = len (stringlist)
        dist = {}
        dist2 = {}

        for i,v in enumerate(pattern):
            st = stringlist[i]
            if v in dist and dist[v] != st:
                return False
            if st in dist2 and dist2[st] != v:
                return False
            if v not in dist:
                dist[v] = st
            if st not in dist2:
                dist2[st] = v
        
        
        return True

s = Solution()
pattern = 'abba'
st = 'dog dog dog dog'

if s.wordPattern(pattern, st):
    print('match')
else:
    print('not match')

        