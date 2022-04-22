"""
11. Container With Most Water
Medium

16211

919

Add to List

Share
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

i =0, v = 1, a= 0
i =1, v = 8, a = (1 - 0)* min(1,8) = 1
i =2, v = 6, a = 


Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


class Solution:
    def maxArea(self, height:list) -> int:
        maxa =0
        for i,v in enumerate(height):
            if i:
                for j in range(i):
                    a = (i - j) * min(v, height[j])
                    maxa = max(a, maxa)
        return maxa


sol = Solution()
h = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(h))