"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab"

"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ana = {}
        l = len(p)
        ans = []
        dict = {}
        cnt = 0
        for c in p:
            if c in dict:
                dict[c] +=1
            else:
                dict[c] = 1
        print (dict)

        for i,c in enumerate(s):
            if c in p:
                j = i
                while j < i + l:
                    if j == len(s):
                         break
                    if s[j] in p:
                        if s[j] not in ana:
                            ana[s[j]] = 1
                        else:
                            ana[s[j]] += 1
                    else:
                        break
                    j +=1
                print (f'i: {i}, ana {ana}')
                if dict == ana:
                    ans.append(i)
                   

            ana = {}
        
        return ans

sol = Solution()

s = "cbaebabbacd"
p = "abbc"
print (sol.findAnagrams(s,p))
s = "abab"
p = "ab"
#print (sol.findAnagrams(s,p))
                     



        