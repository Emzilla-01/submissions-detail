"""
TLE in naive approach vendor timeboxed practice no search.

The number of ways to pick two different numbers from a, such that their sum is divisible by k.

It is logically correct but time complexity wrong.



later search shows these solutions
https://leetcode.com/problems/count-array-pairs-divisible-by-k/solutions/1784710/python-o-n-k-1-3-easy-code-with-explanation-get-all-factors/?languageTags=python3
https://leetcode.com/problems/count-array-pairs-divisible-by-k/solutions/1784801/python3-factors/
https://leetcode.com/problems/count-array-pairs-divisible-by-k/solutions/3146609/python-short-math/?languageTags=python3


"""

from collections import defaultdict
def solution(a, k):
    cnt=0
    m=defaultdict(set)

    for L in range(len(a)-1):
        R=L+1
        while R<len(a):
            # print("a")
            # check m for a[L]
            _ = m.get(a[L])
            if _:
                # print("b")
                if a[R] in _:
                    cnt+=1
                    continue
            # print("c")
            # check m for a[R]
            _ = m.get(a[R])
            if _:
                # print("d")
                if a[L] in _:
                    cnt+=1
                    continue
            else:     
                # print("e")
                mod_=(a[L]+a[R]) % k
                # print(f"{a[L]}+{a[R]} mod_:{mod_}")
                if not mod_:
                    print("f")
                    m[a[L]].add(a[R])
                    # print(f"added m[{a[L]}]{a[R]}")
                    cnt+=1
            # print(f"\nL:{L} R:{R}, a[L]:{a[L]}, a[R]:{a[R]}, cnt:{cnt}")#\nm`{m.items()}`")
            R+=1
    return(cnt)