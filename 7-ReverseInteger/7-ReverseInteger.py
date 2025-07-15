# Last updated: 7/14/2025, 5:50:05 PM
class Solution:
    def reverse(self, x: int) -> int:
        Int_Max, Int_Min =  2**31, -2**31
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if res > (Int_Max - digit) // 10:
                return 0
            res = res * 10 + digit
        return sign * res
