class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        d = None
        sign = '+' 
        ans = 0
        print (s)
        for i, c in enumerate(s):
            if c.isdigit():
                c = int(c)
                if d: d = d * 10 + c
                else: d = c
            elif c in ('*/+-'):
                if sign in '*/': # eager eval
                    ans = self.eval(ans, d, sign)
                    sign = c
                    d = None
                elif sign in '+-': # lazy eval, just add to stack
                    stack.append(ans)
                    if sign == '-':
                        d = -d                    
                    ans = d
                    sign = c
                    d = None
        print (stack)
        if sign in '*/':
            ans = self.eval(ans, d, sign)
            stack.append(ans)
        elif sign in '+-':
            stack.append(ans)
            if sign == '-':
                d = -d
            stack.append(d)   

        print (stack)

        while len(stack) > 1:
            d = stack.pop()
            stack[-1] = self.eval(stack[-1], d, '+')
        return stack[0]

    def calc(self, s:str) -> int:
        sign = '+'
        ans = 0
        d = None
        st = []
        for i,c in enumerate(s):
            if c.isdigit():
                c = int(c)
                if d:
                    d = 10 * d + c
                else:
                    d = c
            elif c in '+-':
                ans = self.eval(ans, d, sign)
                d = None
                sign = c
            elif c in '(':
                st.append(ans)
                st.append(sign)
                d = None
                sign = '+'
                ans = 0
            elif c == ')':
                ans = self.eval(ans, d, sign) 
                d = ans
                sign = st.pop()
                ans = st.pop() 


        return self.eval(ans, d , sign)

    def eval (self,a:int, b:int, op:str)->int:    
        ans = 0
        if op == '+':
            ans=  a+b
        if op == '-':
            ans = a-b
        if op == '*':
            ans = a*b
        if op == '/':
            ans = a//b
        return ans
        
s = Solution()
print (s.calculate('10+3-5 *2+3 -7*6+10/5+ 12*9/3+11-3*2+7*7'))
print (s.calculate('4+3* 3+ 1'))
print(s.calculate('4*3* 9/3 *6* 5'))
#print(s.calc('2+  4  -5     +7 -6'))
#print(s.calc('2 + (( 6 - 2 +5 +11 ) + 7) -23 +(51 - 17)'))