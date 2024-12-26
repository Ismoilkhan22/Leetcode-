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

# def hasDublicate(nums: List[int]) -> bool:
#     return len(set(nums))< len(nums)

# print(hasDublicate([1,2,3,3]))




"""
    problem 2    
"""

"""
Given two strings s and t, return true if the two strings are anagrams of each other,
otherwise return false.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.
Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false


"""
# solution1


# def isAnagram(s: str, t: str) -> bool:
#     return sorted(s) == sorted(t)


# solution2

# def isAnagram(s: str, t: str) ->bool:
#         if len(s) != len(t):
#             return False
        
#         countS, countT  = {}, {}
        
#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
#         return countS == countT
        
        
# print(isAnagram('racecar', 'carrace'))




# solution2 

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True

print(isAnagram('car', 'rac'))
print(isAnagram('racecar', 'carrace'))