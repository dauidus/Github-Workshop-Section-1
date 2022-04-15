// Solved.
// Runtime: better than 99.83% of JS solutions
// Memory Usage: better than 30.15% of JS solutions

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
  nums.sort((a, b) => a - b);
  var minDiff = 1000;
  var sum;
  for (let i = 0; i < nums.length; i++) {
    let start = i + 1;
    let end = nums.length - 1;
    while (start < end) {
      sum = nums[i] + nums[start] + nums[end];
      if (Math.abs(minDiff) > Math.abs(target - sum)) {
        minDiff = target - sum;
      }
      if (sum < target) {
        start++;
      } else {
        end--;
      }
      if (minDiff === 0) {
        break;
      }
    }
  }
  return target - minDiff;
};

console.log(threeSumClosest([-1, 2, 1, -4], 1));
