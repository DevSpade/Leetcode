class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0,head)
    prev, curr = dummy, head
g
    while curr and curr.next :
        # 위치 저장
        # 1,2번 노드부터 조정하니 그 다음노드를 가르키도록 nextnext
        # second 노드는 현재 노드 다음 것
        nxtPair = curr.next.next
        second = curr.next

        # 이렇게해주면 second는 curr의 1,2 위치가 바뀐게 된다.f
        second.next = curr
        # 이제 바뀐 위치를 second가 2->1 순으로 저장하고 있고,
        # curr에는 그 다음 노드 즉 3번째 노드를 저정한다.
        curr.next = nxtPair

        # 그리고 dummy에는 순서가 바뀐 2->1 순으로 저장된 것을 넣어주고
        prev.next = second

        #update ptrs
        # 
        prev = curr
        curr = nxtPair
    return dummy.next


head = ListNode(1,ListNode(2, ListNode(3, ListNode(4, None))))

swapPairs(head)