
'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.'''

class Solution(object):
    def reverse(self, x):
        
        rev = 0
        y = abs(x)
        while y > 0:
            d = y % 10
            rev = (rev *10) + d
            y = y //10
        if x < 0:
            rev = -1 * rev
        if -2**31 <= rev <= 2**31 - 1:
            return rev
        else:
            return 0    

        