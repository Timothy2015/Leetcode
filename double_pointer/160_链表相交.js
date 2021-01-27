/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

 // Intersection of Two Linked Lists(Easy)

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    var H1 = headA, H2 = headB;
    // 冗余代码-1
    //边界情况处理
    // if (H1===null || H2===null){
    //     return null
    // }

    //a+c+b = b+c+a
    while (H1!==H2){
        // console.log('H1:', H1);
        //---if-else,保证一次只走一步，好的逻辑简化代码！---
        if (H1 === null) {
            H1 = headB;
        }else{
            H1 = H1.next;
        }        
        // console.log('H2:', H2);
        if (H2 === null) {
            H2 = headA;
        }else{
            H2 = H2.next;
        }
        // 冗余代码-2
        // if (H1===null && H2===null){
        //     return null;
        //     // break;
        // }
    }
    return H1;
};