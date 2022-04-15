/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  if (s == null || s.length < 1) return "";
  var start = 0,
    end = 0;
  for (let i = 0; i < s.length; i++) {
    let len1 = middleExpand(s, i, i);
    let len2 = middleExpand(s, i, i + 1);
    let len = Math.max(len1, len2);
    if (len > end - start) {
      start = i - (len - 1) / 2;
      end = i + len / 2;
    }
  }
  return s.substring(Math.ceil(start), end + 1);
};
/**
 *
 * @param {string} string
 * @param {number} lower
 * @param {number} higher
 * @returns {number}
 */
function middleExpand(string, lower, higher) {
  while (
    lower > -1 &&
    higher < string.length &&
    string.charAt(lower) === string.charAt(higher)
  ) {
    lower--;
    higher++;
  }
  return higher - lower - 1;
}
// var longestPalindrome = function (s) {
//   var reverse = s.split("").reverse().join("");
//   if (s === reverse) {
//     return s;
//   }
//   var longestSubPal = "";
//   var currentSubStr = "";
//   var middle = Math.floor(s.length / 2);
//   var iseven = s.length % 2 === 0;
//   if (iseven === false) {
//     let lowerCounter = middle - 1;
//     let upperCounter = middle + 1;

//     currentSubStr = s.charAt(middle);
//     let firstTime = true;
//     while (true) {
//       if (firstTime) {
//         if (currentSubStr === s[lowerCounter]) {
//           currentSubStr = `${currentSubStr}${currentSubStr}`;
//           lowerCounter--;
//         }
//         if (
//           currentSubStr === s[upperCounter] ||
//           currentSubStr === `${s[upperCounter]}${s[upperCounter]}`
//         ) {
//           currentSubStr = `${currentSubStr}${s[upperCounter]}`;
//           upperCounter++;
//         }
//       }
//       firstTime = false;

//       if (s[lowerCounter] === s[upperCounter]) {
//         currentSubStr = `${s[lowerCounter]}${currentSubStr}${s[upperCounter]}`;
//       } else {
//         longestSubPal = replacer(longestSubPal, currentSubStr);
//         break;
//       }
//       lowerCounter--;
//       upperCounter++;
//     }
//     longestSubPal = handleLower(s, longestSubPal, middle - 1);
//     longestSubPal = handleHigher(s, longestSubPal, middle + 1);
//   } else {
//     longestSubPal = handleLower(s, longestSubPal, middle - 1);
//     longestSubPal = handleHigher(s, longestSubPal, middle);
//   }
//   if (longestSubPal === "" && s !== "") {
//     longestSubPal = s[0];
//   }
//   return longestSubPal;
// };

// console.log(
//   longestPalindrome(
//     "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv"
//   )
// );
// console.log(longestPalindrome("ababbbbababba"));
// console.log(longestPalindrome("babad"));
// console.log(longestPalindrome("cbbd"));
// console.log(longestPalindrome("a"));
// console.log(longestPalindrome("ac"));
// console.log(longestPalindrome("caba"));

// console.log(
//   longestPalindrome(
//     "azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc"
//   )
// );
// console.log(longestPalindrome("abbcccbbbcaaccbababcbcabca"));

// function handleLower(s, longestSubPal, midpoint) {
//   var currentSubStr;
//   while (midpoint >= 0) {
//     lowerCounter = midpoint - 1;
//     upperCounter = midpoint + 1;
//     currentSubStr = s[midpoint];
//     var firstTime = true;
//     while (lowerCounter >= 0) {
//       if (firstTime) {
//         if (currentSubStr === s[lowerCounter]) {
//           currentSubStr = `${currentSubStr}${currentSubStr}`;
//           lowerCounter--;
//         }
//         if (
//           currentSubStr === s[upperCounter] ||
//           currentSubStr === `${s[upperCounter]}${s[upperCounter]}`
//         ) {
//           currentSubStr = `${currentSubStr}${s[upperCounter]}`;
//           upperCounter++;
//         }
//       }
//       firstTime = false;
//       if (s[lowerCounter] === s[upperCounter]) {
//         currentSubStr = `${s[lowerCounter]}${currentSubStr}${s[upperCounter]}`;
//       } else {
//         longestSubPal = replacer(longestSubPal, currentSubStr);
//         break;
//       }
//       lowerCounter--;
//       upperCounter++;
//       longestSubPal = replacer(longestSubPal, currentSubStr);
//     }
//     midpoint--;
//   }
//   return longestSubPal;
// }

// function handleHigher(s, longestSubPal, midpoint) {
//   while (midpoint < s.length - 1) {
//     var firstTime = true;
//     lowerCounter = midpoint - 1;
//     upperCounter = midpoint + 1;
//     currentSubStr = s[midpoint];
//     while (upperCounter <= s.length - 1) {
//       if (firstTime) {
//         if (currentSubStr === s[lowerCounter]) {
//           currentSubStr = `${currentSubStr}${currentSubStr}`;
//           lowerCounter--;
//         }
//         if (
//           currentSubStr === s[upperCounter] ||
//           currentSubStr === `${s[upperCounter]}${s[upperCounter]}`
//         ) {
//           currentSubStr = `${currentSubStr}${s[upperCounter]}`;
//           upperCounter++;
//         }
//       }
//       firstTime = false;
//       if (s[lowerCounter] === s[upperCounter]) {
//         currentSubStr = `${s[lowerCounter]}${currentSubStr}${s[upperCounter]}`;
//       } else {
//         longestSubPal = replacer(longestSubPal, currentSubStr);
//         break;
//       }
//       lowerCounter--;
//       upperCounter++;
//     }
//     longestSubPal = replacer(longestSubPal, currentSubStr);
//     midpoint++;
//   }
//   return longestSubPal;
// }

// function replacer(longestSubPal, currentSubStr) {
//   if (longestSubPal.length <= currentSubStr.length) {
//     longestSubPal = currentSubStr;
//   }
//   return longestSubPal;
// }
