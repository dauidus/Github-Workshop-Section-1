// Solved.
// Runtime: better than 97.78% of JS solutions, 76ms
// Memory Usage: better than 27.31% of JS solutions, 41.7 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  var current = nums[0];

  var outer_index = 1;

  while (outer_index < nums.length) {
    let inner_index = outer_index;
    let counter = 0;
    while (inner_index < nums.length && current === nums[inner_index]) {
      counter++;
      inner_index++;
    }
    nums.splice(outer_index, counter);
    current = nums[outer_index++];
  }
  console.log(nums);
  return nums.length;
};

console.log(removeDuplicates([1, 1, 1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]));
console.log(removeDuplicates([1, 1, 2]));
