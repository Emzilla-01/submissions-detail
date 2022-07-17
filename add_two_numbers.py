"""
Runtime: 81 ms, faster than 70.70% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 43.12% of Python3 online submissions for Add Two Numbers.
"""

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