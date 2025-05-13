from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
         
#          for i in range(1,len(nums)):
#             a = target-nums[i]
#             if a in nums:
#                 return [nums.index(i), nums.index(a)]
#             else :
#                 return None

# nums = [3,2,4]
# target = 6
# solution = Solution()

# print(solution.twoSum(nums, target))
    

# two sum problem

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#        n = len(nums)
#        numMap = {}
#        neg = 0
#        for i in range(n):
#            neg = target-nums[i]
#            if neg in numMap:
#                return [numMap[neg], i]
#            numMap[nums[i]] = i
           
# nums = [3,2,4]
# target = 6
# solution = Solution()

# print(solution.twoSum(nums, target))






# 2.  remove dublicate from sorted array problems 26 from leetcode

class Solution:
    def removeDublicates(self, nums):
        p = sorted(set(nums))
        k = len(p)

        for i in range(0,k):
            nums[i]=list(p)[i]

        return k