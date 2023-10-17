class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gainList = [0]
        index = 0
        for altitude in gain:
            gainList.append(altitude + gainList[index])
            index += 1

        return max(gainList)
        