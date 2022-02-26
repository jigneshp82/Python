from curses.ascii import isdigit


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        st = 0
        sign = 1
        if s[0] == '-':
            sign = -1
            st = 1
        elif s[0] == '+':
            st = 1
        res = 0
        
        for c in s[st:]:
            if not isdigit(c):
                break
            res = 10 * res + ord(c) - ord('0')
        
        res =res * sign

        if res < -2147483648:
             res = -2147483648
             
        
        if res > 2147483647:
            res = 2147483647
            
        return res 

s = Solution()

print (s.myAtoi('   -99999999999999999999'))
print (s.myAtoi('   -143'))
print (s.myAtoi('   143 dfdf '))
print (s.myAtoi(' '))
