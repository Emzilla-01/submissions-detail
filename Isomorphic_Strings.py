'''
Runtime: 45 ms, faster than 89.21% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 14.1 MB, less than 89.36% of Python3 online submissions for Isomorphic Strings.
https://leetcode.com/problems/isomorphic-strings/submissions/
My solution is called `First occurence transformation` by lc docs.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d=dict()
        for i in range(len(s)):
            if d.get(s[i]):
                "key already exists"
                "must match"
                if d[s[i]]==t[i]:
                    pass
                    'good'
                else:
                    return(False)
            else:
                if t[i] in d.values():
                    return(False)
                d[s[i]]=t[i]
        return(True)           
