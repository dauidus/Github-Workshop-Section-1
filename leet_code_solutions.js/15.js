// Solved.
// Runtime: better than 73.9% of JS solutions
// Memory Usage: better than 98.99 % of JS solutions

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  var returnArray = [];
  var start;
  var end;
  var targetSum;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === nums[i - 1]) {
      continue;
    }
    targetSum = -nums[i];
    start = i + 1;
    end = nums.length - 1;

    while (start < end) {
      let sum = nums[start] + nums[end];
      if (sum === targetSum) {
        returnArray.push([-targetSum, nums[start], nums[end]]);
        start++;
        end--;
        while (start < end && nums[start] === nums[start - 1]) {
          start++;
        }
        while (start < end && nums[end] === nums[end + 1]) {
          end--;
        }
      } else if (sum > targetSum) {
        end--;
      } else if (sum < targetSum) {
        start++;
      }
    }
  }
  return returnArray;
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
