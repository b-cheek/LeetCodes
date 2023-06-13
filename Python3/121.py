from typing import List

class Solution0: # Brute Force, O(n^2)
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for sellIndex in range (1, len(prices)):
            for buyIndex in range(0, sellIndex):
                if prices[sellIndex] - prices[buyIndex] > maxProfit: maxProfit = prices[sellIndex] - prices[buyIndex]
        return maxProfit
    
class Solution1: # Recursive, O(n^2) Don't even know what's going on here lol
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = len(prices)-1
        maxPrice = 0
        for i in range (0, len(prices)):
            if prices[i]<prices[minPrice]: minPrice = i
            elif prices[i]>prices[maxPrice]: maxPrice = i

        if minPrice>maxPrice: return prices[maxPrice] - prices[minPrice]
        prices.pop(minPrice)
        prices.pop(maxPrice)
        return maxProfit(prices)

class Solution2: # This solution I think uses Kadane's Algorithm but with indices, O(n)
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit

class Solution3: # Smarter implementation of Kadane's Algorithm, O(n)
    def maxProfit(self, prices: List[int]) -> int:
        maxCur = 0
        maxSoFar = 0
        for i in range(1, len(prices)):
            maxCur += prices[i]
            maxCur = max(0, maxCur - prices[i-1]) ## Sell value - buy value
            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar

class Solution4: # Same as Solution3 but with a list of differences, O(n)
    def maxProfit(self, prices: List[int]) -> int:
        diffList = [0] + [prices[i]-prices[i-1] for i in range(1, len(prices))]
        
        maxProfit = profit = 0

        for buyIndex in range(len(prices)):
            profit = max(profit + diffList[buyIndex], 0)
            if profit>maxProfit: maxProfit = profit

        return maxProfit
        
s = Solution2()
prices = []