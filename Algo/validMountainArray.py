
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
                        flip = 1
                        slop = -1
                        continue
                    else:
                        return False
                if diff < 0 and slop == -1: continue

        return True





s= Solution()
arr = [0,2,2,1,3,2,1]
if (s.validMountainArray(arr)):
    print('Mountain')
else:
    print ('no Mountain')