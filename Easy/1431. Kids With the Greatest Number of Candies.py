class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result =[]

        for index, num in enumerate(candies):
            candies[index] = num + extraCandies

            if candies[index] == max(candies):
                result.append(True)
            else:
                result.append(False)
            
            candies[index] = num

        return result
