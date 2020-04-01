"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
             return None
        cur=head
        while cur:
            tmp =cur.next
            cur.next=Node(cur.val,None,None)
            cur.next.next=tmp
            cur=tmp
        cur=head
        while cur:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next

        a=head.next
        tmp=a
        while tmp.next:
            head.next=head.next.next
            head=head.next
            tmp.next=tmp.next.next
            tmp=tmp.next
        tmp.next=None
        return a
