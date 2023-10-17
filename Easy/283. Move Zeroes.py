class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for num in nums:
            if num == 0:
                locationOfZero = nums.index(num)
                nums.append(num)
                nums.remove(num)