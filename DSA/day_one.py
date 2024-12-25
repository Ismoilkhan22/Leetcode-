# problem
"""
Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

"""
from typing import List


# solution1


# def hasDuplicate(nums: List[int]) -> bool:
#     a = set()
#     for i in nums:
#         if i in a:
#             return True
#         a.add(i)
#     return False

#
# b = [1, 2, 3, 4, 4]
# print(hasDuplicate(b))

# solutions2

# def hasDuplicate(nums: List[int]) -> bool:
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False


# b = [1, 2, 3, 4]
# print(hasDuplicate(b))

# solutions3

# def hasDublicate(nums: List[int]) -> bool:
#     nums.sort()
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i-1]:
#             return True
#     return False

# solutions4  shakaladni yechim.

def hasDublicate(nums: List[int]) -> bool:
    return len(set(nums))< len(nums)

print(hasDublicate([1,2,3,3]))