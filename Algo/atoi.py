from curses.ascii import isdigit


class Solution:
    def myAtoi(self, s: str) -> int:
        d = 0
        neg = False
        for c in s:
            if c.isdigit():
                c = int(c)
                d = d * 10 + c
            elif c == '-':
                if d == 0:
                    neg = True
            elif c in '+ ':
                continue
            else:
                break
        if neg:
            d = -d

        if d < -2147483648:
             d = -2147483648
        
        if d > 2147483647:
            d = 2147483647

        return(d)

s = Solution()

print (s.myAtoi('   99999999999999999999'))
print (s.myAtoi('   +1'))
