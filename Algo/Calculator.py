"""
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation.
'-' could be used as a unary operation but it has to be inside parentheses.
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.


Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

"""

class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        ans = 0
        stack = []
        i =0
        num = 0

        while i < len(s):
            if s[i].isdigit():
                j = i
                num = 0
                while j < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    j += 1
                ans += ans * sign
                i = j
                ans = ans * sign
            if s[i] == '+':
                sign = 1
                i +=1
            if s[i] == '-':
                sign = -1
                i +=1
            if s[i] =='(':
                stack.append(ans)
                stack.append(sign)
                sign = 1
                ans = 0
            if s[i] ==')'







    def operation(self, s: str) -> int:
        i = 0
        n = len(s)
        op = None
        d1 = None
        d2 = None
        for i in range(n):
            if s[i] not in ('+','-'):
                if op:
                    if d2:
                        d2 += s[i]
                    else:
                        d2 = s[i]
                else:
                    if d1:
                        d1 += s[i]
                    else:
                        d1 = s[i]
            else:
                op = s[i]
            print (f'op: {op} , d1 : {d1}, d2 : {d2}')
            if op and d1 and d2:
                if op == '+':
                    ans =  self.add(d1,d2)
                else:
                    ans = self.minus(d1,d2)
                op = None
                d1 = ans
                d2 = None  
        print(s)
        return ans

    def add(self,d1, d2):
        return (int(d1)+int(d2))

    def minus(self,d1,d2):
        return (int(d1)-int(d2))

sol = Solution()

s = '(1+(4+5+2)-3)+(6+8)'
print(sol.calculate(s))