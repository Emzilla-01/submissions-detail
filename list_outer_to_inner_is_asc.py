"""
Can alternating array be sorted strictly ascending?

all tests passed.

"""

def solution(a):
    # print(a)
    if len(a) <=1:
        return(True)
    L=0
    R=len(a)-1
    while L<=R:
        # print(f"a[L]:{a[L]}")
        # print(f"a[R]:{a[R]}")
        # print(f"`{a[L]}` < `{a[R]}` :{a[L] < a[R]}")
        
        if a[L] == a[R]:
            # if equal check if they are accessing same ix
            # check if it is middle
            if len(a)%2==1:
                if L+1 == len(a)//2+1:
                    # print(f"middle at L:{L}, len(a):{len(a)}")
                    if a[L]>a[R+1]:
                        # print(f"curr `{a[L]}` greater than last `{a[R+1]}` ")
                        return(True)
                    else:
                        return(False)
            else:
                return(False)
                
        if not a[L] < a[R]:
            return(False)
        if R<len(a)-1:
            if a[L] == a[R+1]:
                return(False)
        # if 
        L+=1
        R-=1
    return(True)
    """
    
    Your task is to determine whether the new array b is sorted in strictly ascending order or not
    
    we can compare with out actually making new list
    a = [1, 3, 5, 6, 4, 2]
         L              R
         True
            L        R
            True
               L  R
               True
                   
    """
    
    