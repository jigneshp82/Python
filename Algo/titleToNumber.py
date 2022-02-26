"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans =0
        for i,c in enumerate(columnTitle):
            ans = 26 * ans + ord(c) - ord('A') +1
        return(ans)


s = Solution()
print(s.titleToNumber('ZY'))
print (ord('0'))
print (ord('9'))
print (ord('+'))
print (ord('-'))
print (chr(44))
print(chr(46))
print (chr(47))