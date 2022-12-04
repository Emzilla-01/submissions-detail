'''
https://leetcode.com/problems/is-subsequence/submissions/

Intuitively, a two-pointer, but there are divide & conquer, hashmap, & Levenshtein distance matrix solutions as well.
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        if s =="":
            return(True)
        while (i<len(s)) and (j<len(t)):
            if s[i]==t[j]:
                i+=1
                j+=1
                continue
            j+=1
        if i==len(s):
            return(True)
        return(False)

if __name__=='__main__':
    s=Solution()
    print(
        s.isSubsequence("abc", "ahbgdc")
    )