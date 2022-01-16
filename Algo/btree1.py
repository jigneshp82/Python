
class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        stack = []
        dict = {}
        for i, n in enumerate(nums2):
            if len(stack) ==0:
                stack.append(n)
            else:
                while n > stack[-1]:
                    se = stack.pop()
                    dict[se] = n
        print (stack)
        print (dict)

nums1 = [4,1,2]
nums2 = [1,3,4,2]
