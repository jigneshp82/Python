"""
856. Score of Parentheses
Medium

3856

118

Add to List

Share
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.


s = w(((a)))((b)(p(q)))(c)(d)
s = 0+((1))+(1+(p.1))+1+1
s = 0+(2)+(1+2)+2
s = 0+4+6+2
s = 12

cnt = 0
ans = 0
w : -
( : cnt +=1 , cnt = 1, ans = 0
( : cnt +=1 , cnt = 2, ans = 0
( : cnt +=1 , cnt = 3 ans = 0
a : -
) : ans += pow(2,cnt -1), cnt -=1, ans = 4, cnt =2
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0 
        cnt = 0
        for ch in s:
            if ch == '(':

        