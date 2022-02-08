"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
"""

class Solution:
    def addDigits(self, num: int) -> int:

        ans = num
        while ans > 9:
            ans = str(ans)
            sum = 0
            for d in ans:
                sum = sum + int(d)
            ans = int(sum)
        return(ans)
    def addDigits2(self, num: int) -> int:
        if num == 0 : return 0
        if num % 9 ==0 : return 9
        else :return num % 9 

s = Solution()
num = 112389
print(s.addDigits(num))
print(s.addDigits2(num))

