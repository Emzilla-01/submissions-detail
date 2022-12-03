#https://leetcode.com/problems/find-pivot-index/submissions/

from typing import List

class Solution1:
    '''
    memoize r pass

    do not memoize l pass

    Runtime: 484 ms, faster than 12.91% of Python3 online submissions for Find Pivot Index.
    Memory Usage: 18.5 MB, less than 11.41% of Python3 online submissions for Find Pivot Index.
    
    Top performing answers on lc are similar. It is a two-pass but best solution is use dict[sum]=List[index].
        There is another- assign sum() whole input, then iterate left to right comparing sum_left to curr.

    '''
    def pivotIndex(self, nums: List[int], v:bool=None) -> int:
        d=dict()
        print(nums)        
        # right pass
        su=0
        for i in range(len(nums)-1, -1, -1):
            
            if i == len(nums)-1:
                d[i]={'rsum':0}
                
            else:
                su=sum((su,nums[i+1]))
                d[i]={'rsum':su}
            if v:
                print(f"{i}, {d[i]}, su: {su}")
        del i
        # left pass
        su=0        
        for i in range(len(nums)):
            if i < 1:
                su=0                
            else:
                su+=nums[i-1]
            if v:
                print(f"{i}, {d[i]}, su: {su}")

            if su==d[i]['rsum']:
                return(i)

        print(f"final state of d:{d}")
        return(-1)


class Solution0:
    '''
    Runtime: 779 ms, faster than 8.44% of Python3 online submissions for Find Pivot Index.
    Memory Usage: 19.3 MB, less than 11.41% of Python3 online submissions for Find Pivot Index.
    '''
    def pivotIndex(self, nums: List[int], v:bool=None) -> int:
        d=dict()
        print(nums)        
        # right pass
        su=0
        for i in range(len(nums)-1, -1, -1):
            
            if i == len(nums)-1:
                d[i]={'rsum':0}
                
            else:
                su=sum((su,nums[i+1]))
                d[i]={'rsum':su}
            if v:
                print(f"{i}, {d[i]}, su: {su}")
        del i
        # left pass
        su=0        
        for i in range(len(nums)):
            if i < 1:
                d[i].setdefault('lsum',0)
                print(f"{i}: {d[i]}")
                
            else:
                su+=nums[i-1]
                d[i].setdefault('lsum', su)
            if v:
                print(f"{i}, {d[i]}, su: {su}")

            if d[i]['lsum']==d[i]['rsum']:
                return(i)

        print(f"final state of d:{d}")
        return(-1)
        


if __name__ == '__main__':
    s= Solution1()

    [print(i) for i in [
        s.pivotIndex([1,7,3,6,5,6],v=1),
        s.pivotIndex([1,2,3],v=1),
        s.pivotIndex([2,1,-1],v=1),        
                        ]
    ]

     