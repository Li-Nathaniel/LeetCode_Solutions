class Solution:
    def pivotIndex(self, nums: List[int]) -> int: 
        leftSum = 0
        rightSum = sum(nums)

        for index, num in enumerate(nums):
            rightSum -= num

            if leftSum == rightSum:
                return index

            leftSum += num
        
        return -1