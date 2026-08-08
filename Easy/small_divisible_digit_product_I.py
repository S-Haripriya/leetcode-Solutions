
''' You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t. '''

class Solution(object):
    def smallestNumber(self, n, t):
        num = n
        product = 1
        while n > 0 :
            d = n%10
            product *= d
            n = n // 10
            if n != 0:
                continue
            if product % t == 0:
                return num
            else:
                n = num +1
                num = n
                product = 1
    

        