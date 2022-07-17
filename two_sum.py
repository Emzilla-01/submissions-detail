"""
Runtime: 63 ms, faster than 92.80% of Python3 online submissions for Two Sum.
Memory Usage: 15.5 MB, less than 9.08% of Python3 online submissions for Two Sum.

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        possible_answers_dict = dict()
        
        for i in range(len(nums)):
            curr_val = nums[i]
            
            try_keys = possible_answers_dict.get(curr_val)
            
            if try_keys != None:
                return([try_keys,i])
            
            possible_answers_dict[target - curr_val] = i