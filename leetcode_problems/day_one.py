from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         
         for i in range(1,len(nums)):
            a = target-nums[i]
            if a in nums:
                return [nums.index(i), nums.index(a)]
            else :
                return None

nums = [3,2,4]
target = 6
solution = Solution()

print(solution.twoSum(nums, target))
    


