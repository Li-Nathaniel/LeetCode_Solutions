class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Only = set(nums1)
        bothSet = set()
        nums2Only = set()
        for num in nums2:
            if num in nums1Only:
                nums1Only.remove(num)
                bothSet.add(num)
            elif num not in bothSet:
                nums2Only.add(num)
        return [list(nums1Only), list(nums2Only)] 