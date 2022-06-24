# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
seems most efficient method would be 

to create the outermost to innermost product

while iterating across both linked lists at the same time

when one is exhausted, take the remaining value at the inner ix


however, let's try a quick and dirty approach to get correct answers 

-> could fail time complexity, but better to start with correct and brute, then gain efficiency

#
get_val(ln:ListNode=None):
    if ln == None:
        return(0)
    else:
        return(ln.val)
        
# Outer iteration condition
while any(
    [
    curr_l1 not None,
    curr_l2 not None
    ]
    ):
# Carry 10s to next sum
                        # (7+7)//10 , (7+7)%10
next_sum, curr_sum = (next_sum + curr_l1 + curr_l2)//10 , (next_sum + curr_l1 + curr_l2)%10

# build linked list as we gather sums


"""

n_ = lambda t_ : t_.next

class Solution:    
    def iter_to_list(self, l_:ListNode)->list:
        """ conjoin linked list from final ListNode
        eg: 
        iter_to_list(
                ListNode{val: 2 next:
                    ListNode{val: 4, next:
                        ListNode{val: 3, next: None}
                            }
                        }
                    )
        ->
        [3,4,2]        
        """
        list_ = list()

        curr_l = l_
        
        while curr_l != None:
        
            #print(f"curr_l.val: {curr_l.val}, curr_l.next: {curr_l.next}")
            
            list_.insert(0, curr_l.val)
            
            curr_l = curr_l.next
            
        return(list_)

    def list_to_str_to_int(self, l0: list=None) -> int:
        return(
            int("".join(
                [str(n) for n in l0]
            )
               )
        )
    
    def int_to_str_to_ll_ints(self, int_ : int=None) -> ListNode:
        s_ = str(int_)
        lst_ = list(s_) # [::-1]
        a_ = None
        for i in range(len(lst_)):
            a_=ListNode(val=lst_[i], next=a_)
        return(a_)
            
        

    def get_sums(self, l1,l2)->int:
        sum_ = self.list_to_str_to_int(self.iter_to_list( l1 )) + self.list_to_str_to_int(self.iter_to_list( l2 ))
        return(sum_)

    
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return(
            self.int_to_str_to_ll_ints(
                self.get_sums(
                    l1,
                    l2)
                )
            )
"""
Runtime: 81 ms, faster than 70.70% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 43.12% of Python3 online submissions for Add Two Numbers.
"""


################
# import inspect
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    #def reverse_str(s:str=None) -> str:
    #    pass
    
    #def str_to_int(s:str=None) -> int:
    #    try:
    #        return(int(str))
    #    except ValueError as e:
    #        i_= inspect.stac()
    #        print("{type(e) : e} Excepti0n! in {i_[0][3], i_[1][3], __name__}")
    #        return("")
            
    #def list_to_str(l:list=None) -> str:
    #    return(
    #        "".join([str_to_int(c) for c in l[::-1]])
    #    )
    
    iters = 0
    int_val*10**iters
    

    iters+=1 # in iteration
    
    (l1.value*10**iters) + (l2.value*10**iters)
    
    l_.append( sum()  )
    
    # since lists may be differen len, we should take one pass over each instead of iterating over both..?
    
    
    return( sum(l_) )
    
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass
    
################