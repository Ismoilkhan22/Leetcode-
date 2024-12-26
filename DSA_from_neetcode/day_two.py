# two sum .

"""
masala sharti .

  Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
    """



# my solution.


from typing import List



# nums = [1,2,3,4,5,6,7]
# target = 34

# def twoSum(nums: List[int], target: int) ->List[int]:
#     a = []
#     for i in range(0, len(nums)):
#         b = target-nums[i]
#         if b in a:
#             return [nums.index(b),i]
#         else:
#             a.append(nums[i])
#      return []
    
    
# print(twoSum([1,2,3,5],6))


# i learned solutions.

# 1 .  brute force 

# def twoSum(nums: List[int], target: int) ->List[int]:
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j] == target:
#                 return [i, j]
#     return []

# print(twoSum([1,2,3,5],4))


# 2. sorting . 

# def twoSum(nums: List[int], target: int) ->List[int]:
#     A = []
#     for i, num in enumerate(nums):
#         A.append([num, i])
    
#     A.sort()
#     i, j = 0, len(nums)-1
#     while i<j:
#         cur = A[i][0]+A[j][0]
#         if cur == target:
#             return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
#         elif cur < target:
#             i+=1
#         else:
#             j -=1
            
#     return []
    
    

# 3 hash map (two pass)

# def twoSum(nums: List[int], target: int) ->List[int]:
#     indices = {}
    
#     for i, n in enumerate(nums):
#         indices[n] = i
        
#     for i, n in enumerate(nums):
#         diff = target-n
#         if diff in indices and indices[diff] !=i:
#             return [i, indices[diff]]


# 4 hash map (one pass)
def twoSum(nums: List[int], target: int) ->List[int]:
    prewMap = {}  # bo'sh hash map yaratish

    for i, n in enumerate(nums):  # enumerate orqali i index va n qiymatni nums listidan olish
        diff = target-n   # ayirmani baxolash 
        if diff in prewMap: # agar diff prewMap da bo'lsa yechim mavjud u prewmap dictda n olingan index va i indexdagi son
            return[prewMap[diff], i]
        prewMap[n] = i 









