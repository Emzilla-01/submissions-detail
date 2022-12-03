'''
https://leetcode.com/problems/running-sum-of-1d-array/submissions/
Runtime: 47 ms, faster than 85.22% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 13.9 MB, less than 99.60% of Python3 online submissions for Running Sum of 1d Array.
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        su=0
        for i in range(len(nums)):
            su+=int(nums[i])
            nums[i]=su
        return(nums)