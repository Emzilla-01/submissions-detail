from typing import List, Optional
#from functools import reduce

VERBOSE=False

def printf(o:object,v_:bool=VERBOSE)->None:
    if v_:
        print(o)

def flatten(l:List,
     tmp_vals:List=list(),
     )->List[int]:
     """
     return flat list"""
     next_itrbl = list()
     for itm in l:
        printf(f"itm:`{itm}`")
        t_itm=type(itm)
        if type(itm) == list:
            for itm1 in itm:
                next_itrbl.append(itm1)
        if t_itm == int:
            
            tmp_vals.append(itm)
            printf("tmp_vals")
     if len(next_itrbl)<1:
        return(tmp_vals)    
     else:
        # recurse on next_itrbl but retain values
        printf(f"len(next_itrbl): `{len(next_itrbl)}` tmp_vals:`{tmp_vals}`\n")
        return( tmp_vals + flatten(l=next_itrbl,tmp_vals=list()) )
        
        
def flatten1(l:List,
        rs:int=0,
        )->int:
    """return sum"""
    next_itrbl = list()
    for itm in l:
        printf(f"itm:`{itm}`")
        t_itm=type(itm)
        if type(itm) == list:
            for itm1 in itm:
                next_itrbl.append(itm1)
        if t_itm == int:
            rs+=itm
            printf(f"rs:`{rs}`")
    if len(next_itrbl)<1:
        return(rs)
    else:
        # recurse on next_itrbl but retain values
        printf(f"len(next_itrbl): `{len(next_itrbl)}`")
        return(rs+flatten1(l=next_itrbl))



################################################################################
if __name__ == "__main__":
    dta = [1,2,'a',[3,4,'b',[None,5,6,['spam',7,8]]],['test']+[i for i in range(29,33)], RecursionError]

    print(flatten(dta))

    print("#"*80)

    print(flatten1(dta))