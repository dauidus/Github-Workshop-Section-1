// Solved.
// Runtime: better than 98.56% of JS solutions
// Memory Usage: better than 59.52% of JS solutions

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  var currentNode = head;
  var totalSize = 0;

  while (currentNode) {
    totalSize += 1;
    currentNode = currentNode.next;
  }
  var distance = totalSize - n;
  currentNode = head;
  if (distance === 0 && totalSize === 1) {
    head = null;
    return head;
  } else if (distance === 0) {
    head = head.next;
    return head;
  }
  while (distance > 1) {
    currentNode = currentNode.next;
    distance--;
  }
  currentNode.next = currentNode.next.next;

  return head;
};
