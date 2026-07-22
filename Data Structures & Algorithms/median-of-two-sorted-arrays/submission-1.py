class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1+nums2)
        l, r = 0, len(nums3)
        m = (l+r)//2
        if len(nums3) % 2 == 0:
            return (nums3[m] + nums3[m-1]) / 2
        else:
            return nums3[m] / 1