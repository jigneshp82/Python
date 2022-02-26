"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""



class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.res = []
        self.checkcombination(candidates,target,0,[], 0 )
        return self.res
        
    def checkcomb1(self, candidates: list[int], target :int, currsum :int, sublist:list[int], index : int):
        print (sublist)
        if currsum > target:
            return
        if currsum == target:
            self.res.append(sublist)
            return
        for i in range(len(candidates)):
            self.checkcomb2(candidates[i:], target, currsum + candidates[i], sublist + [candidates[i]], 0)


    def checkcombination(self, candidates: list[int], target :int, currsum :int, sublist:list[int], index : int):

        if index > len(candidates) or currsum > target:
            return
        
        if currsum == target:
            newsublist = [i for i in sublist]
            self.res.append(newsublist)
            return       
        
        
        for i in range(index, len(candidates)):
            sublist = sublist + [candidates[i]]
            currsum = sum(sublist)
            self.checkcombination(candidates,target,currsum, sublist, i)
            sublist.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.res2 = []
        self.checkcomb2(candidates,target, 0, [])

    def checkcomb2(self, nums, target, currsum, sublist):
        if currsum > target:
            return
        if currsum == target:
            self.res2.append(sublist)
            return

        for i in range(len(nums)):
            self.checkcomb2(nums[i+1:], target, currsum + nums[i], sublist + [nums[i]])




s = Solution()
c = [2,3,6,7]
t = 7
r = s.combinationSum(c,t)
print(r)
n = [10,1,2,7,6,1,5]
target = 8
#r2 = s.combinationSum2(n,target)
#print(r2)