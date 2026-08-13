
'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.'''

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        distance = len(height) -1 
        area = 0
        while left < right:
            h = min(height[left],height[right])
            area = max(area,h * distance)
            if height[left] < height[right] :
                left +=1
            else:
                right -=1
            distance -=1            
        return area