# Best Time to Buy and Sell Stock

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

class Solution3: # Smarter implementation of Kadane's Algorithm, O(n). Don't totally understand :(
    def maxProfit(self, prices: List[int]) -> int:
        maxCur = 0 # 
        maxSoFar = 0
        for i in range(1, len(prices)): # Start at 1, i represents sell index
            # As long as you have still made money since the buy date, keep going;
            # If it goes below 0, you wouldn't make that transaction so reset to 0
            # The next two lines of code calculate the profit from the previous day,
            # and set maxCur back to 0 if it's negative
            maxCur += prices[i]
            maxCur = max(0, maxCur - prices[i-1])
            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar

class Solution4: # Same as Solution3 but with a list of differences, O(n)
    def maxProfit(self, prices: List[int]) -> int:
        # the [0] might be unnecessary based on a different (but similar) solution I just did
        diffList = [0] + [prices[i]-prices[i-1] for i in range(1, len(prices))]
        ## Get the difference between each day so maximum subarray problem is more direct

        maxProfit = profit = 0

        for buyIndex in range(len(prices)):
            profit = max(profit + diffList[buyIndex], 0)
            if profit>maxProfit: maxProfit = profit

        return maxProfit


class Solution5: # I think the easiest to understand, maybe not necessarily best? idk.
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            # could use min() here instead, also variable names could be better in this Solution
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

class Solution6: # What I like most recently, similar to S3. actually idk S5 is pretty neat too.
    def maxProfit(self, prices: List[int]) -> int:
        curProfit = maxProfit = 0

        for i in range(1, len(prices)):
            curProfit += (prices[i] - prices[i-1])
            if curProfit < 0:
                curProfit = 0
            else:
                maxProfit = max(curProfit, maxProfit)
        return maxProfit
            

        
s = Solution2()
prices = []