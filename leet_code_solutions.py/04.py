from typing import List


def findMedianSortedArrays(nums1, nums2) -> float:
    nums1.extend(nums2)
    nums1 = sorted(nums1)
    print(nums1)
    if len(nums1) % 2 != 0:
        return nums1[(len(nums1) // 2)]
    else:
        return (nums1[(len(nums1) // 2)] + nums1[(len(nums1) // 2) - 1])/2


print(findMedianSortedArrays([1, 2], [3, 4]))
