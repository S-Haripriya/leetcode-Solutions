'''You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:

The digit sum of n (the sum of its digits).

The digit product of n (the product of its digits).

Return true if n is divisible by this sum; otherwise, return false.'''

class Solution(object):
    def checkDivisibility(self, n):
        sums = 0
        product = 1
        num = n
        while n > 0:
            d = n % 10
            sums += d
            product *= d
            n = n// 10
        total = sums + product    
        if num % total == 0:
            return True 
        else:
            return False       

        