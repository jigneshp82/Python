"""
704. Binary Search
Easy

4177

101

Add to List

Share
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

"""

class Solution:
    
    def search(self, nums: list, target: int) -> int:
        return(self.bsearch(nums, target, 0, len(nums)))

    def bsearch(self, nums:list, t:int, i:int, j:int)->int:        
        if i >= j:
            return -1
        mid = (i + j )// 2
        if nums[mid]== t:
            return mid
        elif nums[mid] < t:
            return(self.bsearch(nums,t, mid+1, j))
        else:
            return(self.bsearch(nums,t,i, mid))

S= Solution()
nums = [-1,0,3,5,9,12]
target = 0
print (S.search(nums,target))