
'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.'''

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) 
        ans = -1
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                ans = mid
                return ans
            elif nums[mid] > target:
                right = mid
                ans = mid

            else:
                left = mid + 1   
                ans = mid           
       
        return left