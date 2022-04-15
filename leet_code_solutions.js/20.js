// Solved.
// Runtime: better than 90.09% of JS solutions
// Memory Usage: better than 11.24% of JS solutions

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  if (s.length === 1) {
    return false;
  }
  var stack = [];
  s = s.split("");

  for (let bracket of s) {
    if (bracket === "{" || bracket === "[" || bracket === "(") {
      stack.push(bracket);
    } else {
      var open = stack.pop();
      if (
        (bracket === "}" && open === "{") ||
        (bracket === ")" && open === "(") ||
        (bracket === "]" && open === "[")
      ) {
        continue;
      } else {
        return false;
      }
    }
  }
  if (stack.length !== 0) {
    return false;
  }
  return true;
};

console.log(
  isValid("[(((((())))))][][][][{{{{{{}}}}}}][(()()()({}{}{}{}{}{})]")
);
console.log(isValid("(("));
console.log(isValid("()"));
