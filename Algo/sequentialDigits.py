from collections import deque


class Solution:
    def sequentialDigits(self, low: int, high: int) -> list:
        l1 = len(str(low))
        l2 = len(str(high))
        ans = []
        s = '123456789'
        while l1 <= l2:
            for x in range(len(s) -l1 +1):
                num = int(s[x:x+l1])
                if low <= num <= high:
                    ans.append(num)
            l1 +=1
        return(ans)
        
            
         


s = Solution()
l = 10
h = 467
print(s.sequentialDigits(l,h))

q =deque(range(1,10))
print (q)
while q:
    c = q.popleft()
    print(c)