from typing import List




class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lower = 0
        upper = len(nums)

        middile = 0

        while lower <= upper:
            middile = (lower+upper)//2
            if nums[middile]< target:
                lower = middile+1
            elif nums[middile] == target:
                return middile

            else :
                upper = middile-1
        return lower   




solution = Solution()
nums = [1,2,3,4,5]
target = 7

print(solution.searchInsert(nums, target))

