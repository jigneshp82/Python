"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
"""


class Solution:
    def validMountainArray(self, arr: list) -> bool:
        slop = 1
        flip = 0 
        for i, v in enumerate(arr):
            if i:
                diff = v - arr[i-1]
                if diff == 0 : return False
                if diff > 0 and slop == 1 : continue
                if diff >0 and slop ==-1: return False
                if diff < 0 and slop == 1:
                    if not flip:
                        if i ==1: return False
                        flip = 1
                        slop = -1
                        continue
                    else:
                        return False
                if diff < 0 and slop == -1: continue

        return True if flip else False





s= Solution()
arr = [0,2,2,1,3,2,1]
if (s.validMountainArray(arr)):
    print('Mountain')
else:
    print ('no Mountain')