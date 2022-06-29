class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    rst = ListNode(None)
    while head and head.next :

        while rst is not None:
            print(rst.val, end = " ")
            rst = rst.next


        rst.val = head.next.val
        rstNext =  ListNode()
        rstNext.val = head.val
        rst.next = rstNext
        
        head.val = head.next.next.val
        head.next = head.next.next.next

        while rst is not None:
            print(rst.val, end = " ")
            rst = rst.next

head = ListNode(1,ListNode(2, ListNode(3, ListNode(4, None))))

swapPairs(head)