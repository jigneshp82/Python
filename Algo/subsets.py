"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        l = len(nums)
        allsubset = []
        for mask in range(1<<l):
            currentsubset = []
            for j in range(l):
                if mask & 1 << j != 0:
                    currentsubset.append(nums[j])
            allsubset.append(currentsubset)
        return(allsubset)
    
    def subsets2(self, nums: list[int]) -> list[list[int]]:
        dp = [[]]
        for n in nums:
            tmp = []
            for x in dp:
                print (f'x : {x}, n : {n}')
                tmp.append(x + [n])
            print (f'tmp:{tmp}')
            dp.extend(tmp)
            print(f'dp: {dp}')
        return dp


s =Solution()
nums = [1,2,3]
print(s.subsets(nums))
print(s.subsets2(nums))