// Solved
// Runtime: 72 ms, faster than 88.39% of JavaScript online submissions for Implement strStr().
// Memory Usage: 40.1 MB, less than 44.22% of JavaScript online submissions for Implement strStr().

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  if (needle === "") return 0;

  if (haystack.includes(needle)) {
    return haystack.indexOf(needle);
  } else {
    return -1;
  }
};
