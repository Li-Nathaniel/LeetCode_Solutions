class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxSell = 0

        for price in prices[1:]:
            maxSell = max(maxSell, price - minBuy)
            minBuy = min(minBuy, price)
        
        return maxSell