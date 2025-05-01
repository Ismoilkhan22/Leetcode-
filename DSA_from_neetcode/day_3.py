
from typing import List

nums = [1,2,3,5,3,4]
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duoble = []
        for i in range(len(nums)):
            if nums[i] in duoble:
                return True
            else:
                duoble.append(nums[i])
        return False

s = Solution()

print(s.hasDuplicate(nums))




