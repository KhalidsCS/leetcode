# A Tough question on leetcode, solved with custom binary search for log(n+m) time :)
# github: KhalidsCS
# problem name: Median of Two Sorted Arrays
import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        idx1 = int(math.floor((len(nums1) - 1) / 2))
        idx2 = int(math.floor((len(nums2) - 1) / 2))

        if (len(nums2) % 2 == 1 and len(nums1) % 2 == 1):
            idx1 -= 1

        max1 = len(nums1) - 1
        min1 = -1
        max2 = len(nums2) - 1
        min2 = -1

        while ((idx2 < len(nums2) - 1 and idx1 < len(nums1) and idx1 >= 0 and nums1[idx1] > nums2[idx2 + 1])
               or (idx1 < len(nums1) - 1 and idx2 < len(nums2) and idx2 >= 0 and nums2[idx2] > nums1[idx1 + 1])):
            if (idx2 < len(nums2) - 1 and idx1 >= 0 and nums1[idx1] > nums2[idx2 + 1]):
                max1 = idx1 - 1
                min2 = idx2 + 1
                idx1 = max((max1 + min1) // 2, idx1 - (len(nums2) - 1 - idx2))
                idx2 += max1 - idx1 + 1
            else:
                max2 = idx2 - 1
                min1 = idx1 + 1
                idx2 = max((max2 + min2) // 2, idx2 - (len(nums1) - 1 - idx1))
                idx1 += max2 - idx2 + 1

        if (len(nums1) + len(nums2)) % 2 == 0:
            if idx1 >= len(nums1) or len(nums1) == 0:
                num1 = nums2[idx2]
            elif idx2 >= len(nums2) or len(nums2) == 0:
                num1 = nums1[idx1]
            else:
                num1 = max(nums1[idx1], nums2[idx2])
            num2 = None
            if idx1 >= 0 and idx2 >= 0:
                num1 = max(nums1[idx1], nums2[idx2])
                num2 = None
                if idx1 >= len(nums1) - 1:
                    num2 = nums2[idx2 + 1]
                elif idx2 >= len(nums2) - 1:
                    num2 = nums1[idx1 + 1]
                else:
                    num2 = min(nums1[idx1 + 1], nums2[idx2 + 1])
            elif idx1 < 0:
                num1 = nums2[idx2]
                if idx1 >= len(nums1) - 1:
                    num2 = nums2[idx2 + 1]
                elif idx2 >= len(nums2) - 1:
                    num2 = nums1[idx1 + 1]
                else:
                    num2 = min(nums1[idx1 + 1], nums2[idx2 + 1])
            else:
                num1 = nums1[idx1]
                if idx1 >= len(nums1) - 1:
                    num2 = nums2[idx2 + 1]
                elif idx2 >= len(nums2) - 1:
                    num2 = nums1[idx1 + 1]
                else:
                    num2 = min(nums1[idx1 + 1], nums2[idx2 + 1])
            return (num1 + num2) / 2

        else:
            if idx1 >= 0 and idx2 >= 0:
                return max(nums1[idx1], nums2[idx2])
            elif idx1 < 0:
                return nums2[idx2]
            else:
                return nums1[idx1]


