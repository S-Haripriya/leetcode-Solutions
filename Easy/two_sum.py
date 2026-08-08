''' You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''


class Solution(object):
    def twoSum(self, nums, target):
        number = {}
        for i in range(len(nums)):
            initial = nums[i]
            value = target - initial
            if value in number:
                return i,number[value]
            else:
                number[nums[i]] = i