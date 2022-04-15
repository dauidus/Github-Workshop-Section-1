// solved
// Runtime: 82 ms, faster than 25.49% of JavaScript online submissions for Remove Element.
// Memory Usage: better than 92.83% of JS online submissions for Remove Element
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
  var counter = 0;
  while (counter < nums.length) {
    if (nums[counter] === val) {
      nums.splice(counter, 1);
    } else {
      counter++;
    }
  }
  return nums.length;
};
