
"""
216. Combination Sum III
Medium

3646

87

Add to List

Share
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
k = 3, n =9, l =[]
l =[1], k = 2, n = 8
l =[1,2], k =1, n = 6
l =[1,2,6]
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> list:
        ans = []
        def getsum(k,n,l,ix):
            if k == 0 and n ==0:
                print (l)
                ans.append(l)
                return
            if k ==0 or n < 0:
                return
            for i in range(ix,10):
                getsum(k-1, n-i, l+[i],i+1)
        getsum(k,n,[],1)
        return(ans)

s= Solution()
k = 3
n = 9
print (s.combinationSum3(k,n))

