from fcntl import DN_DELETE
from math import ceil
import re


class Solution:
    def maxDistToClosest(self, seats: list) -> int:
        l = len(seats)
        dist = seats.index(1)
        res = 0
        for s in seats:
            if s:
                res = max(res, ceil(dist/2))
                dist = 0
            else:
                dist +=1
        return max(dist, res)

            






s = Solution()
seats = [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0]
print(s.maxDistToClosest(seats))
