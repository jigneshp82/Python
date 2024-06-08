###
#Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
#Output: 2
#Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
class Solution:
    def numUniqueEmails(self, emails: list) -> int:
        emailset  = set()
        for e in emails:
            name = e.split('@')[0].split('+')[0].replace('.','')
            domain = e.split('@')[1]
            name = name +'@'+domain
            emailset.add(name)
        return len(emailset)
    
    def oddEvenJumps2(self, arr: list) -> int:
        def getnexthop(sortedidx):
            stack = []
            res = [None] * len(sortedidx)
            for i in sortedidx:
                while stack and i > stack[-1]:
                    res[stack.pop()] = i
                stack.append(i)
            return res
        n = len(arr)

        sortedindex = sorted(range(len(arr)),key = lambda x: arr[x])
        oddindexhop = getnexthop(sortedidx=sortedindex)
        sortedindex.sort(key= lambda x : -arr[x])
        evenindexhop = getnexthop(sortedidx= sortedindex)

        print(f'sortedindex - {sortedindex} , oddindex - {oddindexhop} evenindexhop - {evenindexhop}')
        odd,even = [False]*n, [False]*n
        odd[-1],even[-1] = True, True
        for i in reversed(range(n-1)):
            oddhop , evenhop = oddindexhop[i],evenindexhop[i]
            if oddhop: odd[i] = even[oddhop]
            if evenhop : even[i] =odd[evenhop]
        print(odd, even)

        return sum(odd)

    def oddEvenJumps(self, arr: list) -> int:
        n = len(arr)
        nextoddjump = [0]*n
        stk = []
        for i in  sorted(range(n), key= lambda x: arr[x]):           
            while stk and i >stk[-1]:
                nextoddjump[stk.pop()]= i
            stk.append(i)
        nextevenjump = [0]*n
        stk = []
        for i in sorted(range(n), key = lambda x : -arr[x]):
            while stk and i > stk[-1]:
                nextevenjump[stk.pop()] = i
            stk.append(i)
        print(f'next odd jump {nextoddjump}, next even jump {nextevenjump}')
        odd , even = [0]*n, [0]*n
        odd[-1] = 1
        even[-1] = 1
        for i in range(n-2,-1,-1):
            odd_start , even_start= nextoddjump[i], nextevenjump[i]
            if odd_start:
                odd[i] = even[odd_start]
            if even_start:
                even[i]= odd[even_start]
        print(f'oddstart - {odd} evenstart - {even}  ')
        return sum(odd)
            

            
"""
Input: arr = [2,3,1,1,4]
Output: 3
Explanation: 
From starting index i = 0, wle make jumps to i = 1, i = 2, i = 3:
During our 1st jump (odd-numbered), we first jump to i = 1 because arr[1] is the smallest value in [arr[1], arr[2], arr[3], arr[4]] that is greater than or equal to arr[0].
During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because arr[2] is the largest value in [arr[2], arr[3], arr[4]] that is less than or equal to arr[1]. arr[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3
During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because arr[3] is the smallest value in [arr[3], arr[4]] that is greater than or equal to arr[2].
We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where we can reach the end with some
number of jumps.
"""


s= Solution()
arr =  [10,13,12,14,15,12,17,18,16,13]
print(arr)
print(f'ans - {s.oddEvenJumps(arr)}')
print('---')
print(f'ans - {s.oddEvenJumps2(arr)}')

        