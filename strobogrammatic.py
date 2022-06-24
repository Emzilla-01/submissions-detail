"""
Runtime: 46 ms, faster than 41.86% of Python3 online submissions for Strobogrammatic Number.
Memory Usage: 13.8 MB, less than 97.19% of Python3 online submissions for Strobogrammatic Number.
"""

strobo_dict={
    '0':'0',
    '6':'9',
    '9':'6',
    '8':'8',
    '1':'1',
            }
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # l=list()
        s=''
        for c in num:
            x=strobo_dict.get(c)
            if x == None:
                return(False)
            s=x+s
            # l.insert(0,x)
        # s=''.join(l)
        if s == num:
            return(True)
        return(False)
            