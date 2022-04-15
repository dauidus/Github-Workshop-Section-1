/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  nums1 = nums1.concat(nums2);
  nums1.sort((a, b) => a - b);
  if (nums1.length % 2 != 0) {
    return nums1[Math.floor(nums1.length / 2)];
  } else {
    return (
      (nums1[Math.floor(nums1.length / 2)] +
        nums1[Math.floor(nums1.length / 2) - 1]) /
      2
    );
  }
};

console.log(findMedianSortedArrays([1, 10, 3], [3, 4, 5]));
