
''' Given an integer x, return true if x is a palindrome, and false otherwise. '''

class Solution(object):
    def isPalindrome(self, x):
       digit = x
       number = 0
       while digit > 0:
            modulus = digit % 10
            number = modulus + (number * 10)
            digit = digit // 10
       if number == x:
            return True
       else:
            return False        

        