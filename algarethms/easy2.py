# 20 valid parentheses
"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: fal
"""


 # solutions

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {")": "(", "}": "{", "]": "["}

#         for char in s:
#             if char in mapping.values():
#                 stack.append(char)
#             elif char in mapping.keys():
#                 if not stack or mapping[char] != stack.pop():
#                     return False
#         return not stack


# solutions = Solution()
# s = "{[]}"
# result = solutions.isValid(s)
# print(result)
 


# 21-masala .
#     """
    
# Sizga ikkita tartiblangan bog'langan ro'yxatning boshlari beriladi list1va list2.

# Ikki ro'yxatni bitta tartiblangan ro'yxatga birlashtiring. Ro'yxat birinchi ikkita ro'yxatning tugunlarini birlashtirish orqali tuzilishi kerak.

# Birlashtirilgan bog'langan ro'yxatning boshini qaytaring .

 

# 1-misol:


# Kirish: list1 = [1,2,4], list2 = [1,3,4]
#  Chiqish: [1,1,2,3,4,4]
# 2-misol:

# Kirish: list1 = [], list2 = []
#  Chiqish: []
# 3-misol:

# Kirish: list1 = [], list2 = [0]
#  Chiqish: [0]
 

# Cheklovlar:

# Ikkala ro'yxatdagi tugunlar soni oralig'ida [0, 50].
# -100 <= Node.val <= 100
# Ikkala list1va ham kamaymaydiganlist2 tartibda tartiblangan .
#     """

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = seek
        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next
        return head
