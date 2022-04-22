"""
881. Boats to Save People
Medium

1918

54

Add to List

Share
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 

Constraints:

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
"""

from collections import Counter


class Solution:
    def numRescueBoats(self, people:list, limit: int) -> int:
        boats = 0
        people = sorted(people)
        lo = 0
        hi = len(people)-1
        while lo <= hi:
            if people[lo]+people[hi] <= limit:
                lo+=1
                hi-=1
            else:
                hi-=1
            boats +=1
        return boats
                    


S = Solution()
people = [3,5,3,4]
limit = 5
print(S.numRescueBoats(people, limit))