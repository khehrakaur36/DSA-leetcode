class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        digitsum =0
        digitpro = 1
        while n:
            digit = n%10
            digitsum += digit
            digitpro *= digit
            n = n//10

        return original %(digitsum + digitpro) ==0 