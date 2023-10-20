class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])

        for i in range (len(nums) - k):
            currSum -= nums[i]
            currSum += nums[k + i]
            maxSum = max(currSum, maxSum)

        return maxSum / k