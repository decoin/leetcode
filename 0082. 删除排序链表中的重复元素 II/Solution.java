/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    private int repeatNum = Integer.MAX_VALUE;

    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }

        head.next = deleteDuplicates(head.next);

        if(head != null && head.next != null && head.val == head.next.val){
            repeatNum = head.val;
        }

        while(repeatNum != Integer.MAX_VALUE && head != null && head.val == repeatNum){
            head = head.next;
        }

        return head;

    }
}
