# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or head.next == None:
            return head

        current, length = head, 0    
        while current:
            current, length = current.next, length + 1

        root = ListNode(0)
        root.next = head
        intv = 1

        while intv < length:
            merge_point, current = root, root.next

            while current:

                h1, intv_residue_1 = current, intv
                while intv_residue_1 and current: 
                    current, intv_residue_1 = current.next, intv_residue_1 - 1
                if intv_residue_1:
                    break   
 
                h2, intv_residue_2 = current, intv
                while intv_residue_2 and current: 
                    current, intv_residue_2 = current.next, intv_residue_2 - 1

                len1, len2 = intv, intv - intv_residue_2
                
                while len1 and len2:
                    if h1.val < h2.val: 
                        merge_point.next, h1, len1 = h1, h1.next, len1 - 1
                    else: 
                        merge_point.next, h2, len2 = h2, h2.next, len2 - 1
                    merge_point = merge_point.next

                if len1:
                    merge_point.next = h1  
                else:
                    merge_point.next = h2
                while len1 > 0 or len2 > 0: 
                    merge_point, len1, len2 = merge_point.next, len1 - 1, len2 - 1

                merge_point.next = current

            intv *= 2

        return root.next
