#Given an array of integers arr, you are initially positioned at the first index of the array.
#
#In one step you can jump from index i to index:
#
#i + 1 where: i + 1 < arr.length.
#i - 1 where: i - 1 >= 0.
#j where: arr[i] == arr[j] and i != j.
#Return the minimum number of steps to reach the last index of the array.
#
#Notice that you can not jump outside of the array at any time.
#Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
#Output: 3
#Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
from collections import defaultdict
import collections

class Solution:
    def minJumps(self, arr: list) -> int:
        l = len(arr)
        dict = defaultdict(list)
        nextpos = 0 
        jump = 0
        for i in range(l):
            dict[arr[i]].append(i)

        visited = []
        def bff(node, dist):
            naighbour = set()            
            for n in node:                
                if n in visited: continue
                if n == l - 1 :return dist
                visited.append(n)
                if n: naighbour.add(n-1)
                if n < l -1 : naighbour.add(n+1)                
                if arr[n] in dict:
                    naighbour.update(dict[arr[n]])
                    del dict[arr[n]]
            return (bff(naighbour, dist +1))

        return bff([0], 0)



       

s = Solution()
arr = [100,-23,-23,404,100,23,23,23,3,404]
print(s.minJumps(arr))

arr = [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,11]
print(s.minJumps(arr))
        