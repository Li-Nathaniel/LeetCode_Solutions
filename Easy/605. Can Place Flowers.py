class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spotsAvailable = 0
        if n == 0:
            return True

        if len(flowerbed) == 1:
            return n == 1 and flowerbed[0] == 0

        for index, flower in enumerate(flowerbed):
            if flower == 0:
                if index == 0 and flowerbed[index + 1] == 0:
                    spotsAvailable += 1
                    flowerbed[index] = 1
                elif index == len(flowerbed) - 1 and flowerbed[-2] == 0:
                    spotsAvailable += 1
                    flowerbed[index] = 1
                elif (index != 0 or index != len(flowerbed) - 1) and flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0:
                    spotsAvailable += 1
                    flowerbed[index] = 1
        
        return spotsAvailable >= n