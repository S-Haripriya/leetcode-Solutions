
'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.'''
class Solution(object):
    def strStr(self, haystack, needle):
        left = 0
        right = len(needle)
        
        while right <= len(haystack):
            string = haystack[left:right]
            if string == needle:
                return left
            else:
                left +=1
                right +=1    
        else:
            return -1