# 1-masala
"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if nums[i]+nums[j] == target:
#                     return [i, j]
#         return [] # No solution found
    



# 2- masala 

"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
# """
# class Solution2:
#     def isPalindrome(self, x: int ) ->bool:
#         if  x<0:
#             return False
#         reversed_num = 0
#         temp  = x

#         while temp !=0:
#             digit = temp % 10
#             reversed_num = reversed_num * 10 + digit
#             temp // 10
#         return reversed_num == x 

    

# 3-masala
"""
Rim raqamlari yetti xil belgi bilan ifodalanadi:  I, V, X, L, Cva D.M

Belgi        qiymati
men 1
V 5
X 10
L 50
C 100
D 500
M 1000
Masalan,  Rim raqamida 2yozilganidek II , ikkitasi qo'shiladi. 12kabi yoziladi  XII, bu oddiy X + II. Raqam 27quyidagicha yoziladi XXVII, ya'ni XX + V + II.

Rim raqamlari odatda chapdan o'ngga kattadan kichikga yoziladi. Biroq, to'rt uchun raqam emas IIII. Buning o'rniga to'rt raqami sifatida yoziladi IV. Biri beshdan oldin bo'lgani uchun, biz uni to'rtta qilib ayiramiz. Xuddi shu tamoyil to'qqiz soniga ham tegishli bo'lib, u quyidagicha yoziladi IX. Ayirish qo'llaniladigan oltita holat mavjud:

IV4 va 9 ni hosil qilish uchun (5) va X(10)  dan oldin joylashtirilishi mumkin .
X40 va 90 qilish uchun  L(50) va (100) dan oldin joylashtirilishi mumkin .C
C400 va 900 qilish uchun D(500) va (1000) dan oldin joylashtirilishi mumkin .M
Rim raqami berilgan bo'lsa, uni butun songa aylantiring.

 

1-misol:

Kirish: s = "III"
 Chiqish: 3
 Izoh: III = 3.
2-misol:

Kirish: s = "LVIII"
 Chiqish: 58
 Izoh: L = 50, V= 5, III = 3.
3-misol:

Kirish: s = "MCMXCIV"
 Chiqish: 1994
 Tushuntirish: M = 1000, CM = 900, XC = 90 va IV = 4.
 

Cheklovlar:

1 <= s.length <= 15
sfaqat belgilarni o'z ichiga oladi ('I', 'V', 'X', 'L', 'C', 'D', 'M').
Bus diapazonda haqiqiy rim raqami  ekanligi kafolatlanadi [1, 3999].

"""


# solutions :

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans

