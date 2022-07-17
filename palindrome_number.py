"""Runtime: 89 ms, faster than 62.29% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 58.82% of Python3 online submissions for Palindrome Number."""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return(False)
        s = str(x)
        for i in range(
            (len(s)//2 +1)
            ):
            if not s[i] == s[-(i+1)]:
                return(False)
        return(True)