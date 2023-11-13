class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = {}
        for num in nums:
            if num not in frequencyDict:
                frequencyDict[num] = 1
            else:
                frequencyDict[num] += 1

        sortedDict = dict(sorted(frequencyDict.items(), key=lambda item: item[1], reverse=True))

        return list(sortedDict.keys())[:k]