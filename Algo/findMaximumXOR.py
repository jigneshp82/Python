"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

"""

class TrieNode:
    def _init_(self, val):
        self.child = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, val):
        head = self.root
        for d in val:
            if d not in head.child:
                head.chile[d] =TrieNode()
            head.child = head.child[d]
            
    def check(self,val):
        head = self.root
        


class Solution:
    def findMaximumXOR1(self, nums: list) -> int:
        ans = 0
        i = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans = max(ans, nums[i] ^ nums[j])
        return(ans)

    def findMaximumXOR(self, nums: list) -> int:
        pass

        

s= Solution()
nums = [2,4,8,8,20]
#print (s.findMaximumXOR(nums))


x = 11
print (f'{1<<32} , bin: {bin(1<<32)}')
print (f'bin(x) : {bin(x)}')
print (bin(x|1<<32)[3:])