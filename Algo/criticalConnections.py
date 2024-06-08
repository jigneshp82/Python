"""
1192. Critical Connections in a Network
Hard

4330

156

Add to List

Share
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
"""

class Solution:
    def criticalConnections(self, n: int, connections: list) -> list:
        criticaldict = {}
        criticallist = []
        for i in connections:
            x = i[0]
            y = i[1]

            if x in criticaldict:
                if y not in criticaldict[x]:
                    criticaldict[x].append(y)
            else:
                criticaldict[x]=[y]
            
            if y in criticaldict:
                if x not in criticaldict[y]:
                    criticaldict[y].append(x)
            else:
                criticaldict[y]=[x]

        for key in criticaldict:
            if len(criticaldict[key]) == 1:
                criticallist.append([key,criticaldict[key][0]])

        return criticallist
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
S = Solution()
print(S.criticalConnections(n,connections))



