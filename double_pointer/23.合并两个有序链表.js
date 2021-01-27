/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    //双指针，与合并两个有序数组非常相似
    var H = new ListNode();
    var H1 = l1, H2 = l2, P = H;
    //处理边界
    if (H1===null) {return H2;}
    if (H2===null) {return H1;}

    while (H1!==null && H2!==null){
        if (H1.val <= H2.val){
            P.next = H1;
            P = P.next;
            H1 = H1.next;
        } else{
            P.next = H2;
            P = P.next;
            H2 = H2.next;
        }
    }
    if (H1 !== null){ P.next = H1; }
    if (H2 !== null){ P.next = H2; }
    return H.next;
};