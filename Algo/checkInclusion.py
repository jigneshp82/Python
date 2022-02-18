"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        m = len(s2)
        if l > m:
            return False
        i = 0
        while i < m:
            j = i
            if s2[i] in s1 and i + l < m+1:
                found = True
                while j < j+l -1:
                    print ('----')
                    j+=1
                    print (f'j {j}, j+l {j+l},s2[j]: {s2[j]}')
                    if s2[j] not in s1: 
                        found = False
                        break
                print (found)
                if found:
                    return found
            i +=1
        return False


s1 = "ab"
s2 = "eidboaoobax"
s = Solution()
print(s.checkInclusion(s1,s2))