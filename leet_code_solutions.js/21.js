// Solved.
// Runtime: better than 97.35% of JS solutions
// Memory Usage: better than 65.09% of JS solutions

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
var mergeTwoLists = function (l1, l2) {
  var result;

  if (l1 && l2) {
    if (l1.val >= l2.val) {
      result = l2;
      l2 = l2.next;
    } else {
      result = l1;
      l1 = l1.next;
    }
    result.next = mergeTwoLists(l1, l2);
  } else {
    if (l1 == undefined) {
      result = l2;
    } else if (l2 == undefined) {
      result = l1;
    }
  }
  return result;
};
