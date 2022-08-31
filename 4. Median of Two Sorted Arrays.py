"""Runtime: 167 ms, faster than 32.78% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.3 MB, less than 25.44% of Python3 online submissions for Median of Two Sorted Arrays."""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_median_of_list(l:List[int])->float:
            len_l = len(l)
            if len_l <1:
                return(None)
            if len_l % 2 == 0:
                ixs = ((len(l)-1)//2, len(l)//2)
                m = (l[ixs[0]]+l[ixs[1]])/2
            else:
                m = l[len(l)//2]
            return(m)
        l3 = sorted(nums1+nums2)
        return(get_median_of_list(l3))