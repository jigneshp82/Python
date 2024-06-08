"""
347. Top K Frequent Elements
Medium

8483

354

Add to List

Share
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import Counter


class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        freq = Counter(nums)
        sortedfreq = sorted(freq.items(), key = lambda x : x[1], reverse= True)
        ans = []
        for x in sortedfreq:
            ans.append(x[0])
            if len(ans) == k:
                return ans
            


S = Solution()
nums = [3,0,1,0]
k = 1
print(S.topKFrequent(nums, k))

        