from math import floor, isqrt, sqrt



class Solution:

    def __init__(self):
        self.dp = {}

    def winnerSquareGame(self, n: int) -> bool:
        win = False
        if n ==0:
            return False

        if n in self.dp:
            return self.dp[n]
        

        for i in range(1,isqrt(n)+1):
            x = n - (i **2)
            if x == 0:
                win = True
                break
            else:
                win = win or not(self.winnerSquareGame(x))

        self.dp[n] = win

        return(win)

    def winnerSqureGame2(self, n:int) -> bool :
        DP = [False] * (n + 1)
       
        for i in range(1,n +1):
            DP[i] = any(not DP[i - j * j] for j in range(1, isqrt(i) +1))

        return DP[-1]
        

s= Solution()
n = 8
if s.winnerSqureGame2(n):
    print(f'{n} - win')
else:
    print(f'{n} - loose')