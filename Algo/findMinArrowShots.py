class Solution:
    def findMinArrowShots(self, points:list) -> int:
        sortedlist = sorted(points)
        print(sortedlist)
        a = 0
        region = (float('-inf'),float('-inf'))
        for x1,x2 in sortedlist:            
            if x1 <= region[1]:
                region = (max(x1,region[0]), min(x2,region[1]))
            else:
                region = (x1,x2)
                a +=1
            print (f'x1 {x1}, x2 {x2}, regin: {region}')
        
            
        return a


            
            


        

s = Solution()
arr = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
r = (1,2)
print(r[0])
print(s.findMinArrowShots(arr))

