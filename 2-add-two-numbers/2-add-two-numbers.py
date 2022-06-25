# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_sum = 0
        l2_sum = 0
        idx = 0
        
        while l1 :            
            l1_sum = l1_sum + (l1.val * 10**idx)  
            l1 = l1.next
            idx+=1
        idx = 0 
        while l2 :            
            l2_sum = l2_sum + (l2.val * 10**idx)  
            l2 = l2.next
            idx+=1
            
        total = l1_sum + l2_sum
        reversed_total = str(total)[::-1]
        print(reversed_total)
        
        rst = ListNode()
        pointer = rst
        
        for s in reversed_total :
            pointer.next = ListNode(int(s))       
            pointer = pointer.next
            
        
        print(rst)
        return rst.next