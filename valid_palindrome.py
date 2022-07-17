"""
Runtime: 56 ms, faster than 77.72% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.3 MB, less than 85.60% of Python3 online submissions for Valid Palindrome.
"""

from string import ascii_lowercase, digits
charset=ascii_lowercase+digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ''
        for c in s:
            c1 = c.lower()
            if c1 in charset:
                ns+=c1
        if ns == ns[::-1]:
            return(True)
        else:
            return(False)
#"race a car"
#raceacar
#
