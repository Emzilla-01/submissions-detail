# despite messy, it passed grader cases
# after finding combinatorics for pairs p
"""
>>> from count_pairs import solution
>>> solution([25, 35, 872, 228, 53, 278, 872])
4
"""
from math import factorial
from collections import defaultdict
def count_pairs(n):
    # l=[2,3,4,5]
    if n <=1:
        return(0)
    else:
        a = factorial(n) 
        b = factorial(2)
        p = factorial(n) // (factorial(2)*factorial(n-2))
        # p= a/(b*c)
        #  (n!) / r!(n-r)!
        
        # 4 pairs
        #     3 items
        # 3 == 6 / 2(4-2)!
        # == 24 / 2(4-2)!
        # 6==    24 / 4
        
        # == 120/ 2!(5-2)!
        #     120/2(3)!
        #     120/12    
        # 10 == 120 / # comb = (n!) / r!(n-r)!
        
        
        """
            3 instances: 3 pairs
            4 instances: 6 pairs, 4!==24
            5 instances: 10 pairs, 5!==120
        """
        # print(f"i:{i}, p:{p}, f{factorial(i)}")\
        # print(f"i:{n},f{factorial(n)}, res:{p}")
        return(p)
        

def solution(a):
    m = defaultdict(int)
    for n in a:
        l=sorted([c for c in str(n)])
        s="".join(l)
        m[s]+=1
    cnt = 0
    # print(m)
    for v in m.values():
        """
        3 instances: 3 pairs
        
        1 2 3
        
        1 2
        1   3
          2 3
        
        4 instances: 6 pairs
         4 4 4 4
         1 2
         1   3
         1     4
           2 3
           2   4
             3 4
        
        5 instances... 5 pick 2
        1 2 3 4 5
        1 2
            3
              4
                5
          2 3
              4
                5
            3 4
            3   5
              4 5
        """
        cnt+=count_pairs(v)
    return(cnt)