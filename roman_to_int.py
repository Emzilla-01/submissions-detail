"""Runtime: 75 ms, faster than 51.53% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.9 MB, less than 76.17% of Python3 online submissions for Roman to Integer."""
class Solution:
    def romanToInt(self, s: str) -> int:
                    #value, ix
        val_dict={  'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000,
                 }
        sum_=0
        get_val = lambda c: val_dict.get(c,0)
        for i in range(len(s)):
            try:
                if get_val(s[i+1]) > get_val(s[i]):
                    sum_ -= get_val(s[i])
                else:
                    sum_ += get_val(s[i])
            except IndexError as e:
                sum_ += get_val(s[i])            
        return(sum_)