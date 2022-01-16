
class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        stack = []
        dict = {}
        ans = []
        for n in nums2:
            if len(stack) ==0:
                stack.append(n)
            else:
                while n > stack[-1]:
                    se = stack.pop()                    
                    dict[se] = n
                    if len(stack) ==0:
                        break
                stack.append(n)
        
        while len(stack)>0:
            se = stack.pop()
            dict[se] = -1

        for n in nums1:
            ans.append(dict[n])
    
        return ans

    def nextGreaterElement1(self, nums1: list, nums2: list) -> list:
        stack, dict = [],{}
        for n in nums2:
            while stack and n > stack[-1]:
                stack.pop()
            if stack:
                dict[n] = stack[-1]
            
        print (dict)
        print (stack)

nums1 = [4,1,2]
nums2 = [1,3,4,2]
s = Solution()
print (s.nextGreaterElement(nums1,nums2))

n1 = [8,2,10,7,4]
n2 = [5,8,6,3,2,1,7,10,4]
print (s.nextGreaterElement(n1,n2))
s.nextGreaterElement1(n1,n2)