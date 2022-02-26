from typing import Collection, Counter


class Solution:
    def majorityElement3(self, nums: list[int]) -> int:
        d = Counter(nums)
        ans = []
        for i , v in d.items():
            if v > len(nums)/3:
                ans.append(i)
        return (ans)


    def majorityElement(self, nums: list[int]) -> int:
        count = 1
        me = nums[0]
        for i in nums[1:]:
            print (f'i : {i}, me : {me} , count: {count}')
            if me == i:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                me = i
                count = 1

        return me if count > 0 else None

sol  = Solution()
nums = [4,2,3,3,6,7,3,3,3,2,1,7]
print (sol.majorityElement(nums))