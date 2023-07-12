# Note that a greedy algorithm is best in a "canonical" coin system


# This solution is what I tried at first, helpful for understanding S1 if necessary
# Recursive DFS, exceed runtime. I guess I could've memoized with a helper fn and global table.
# But at that point, it basically becomes tabulation anyway.
class Solution0:
    # Note that I tried to use @cache here, but didn't work saying that the list was unhashable.
    # I just now realized that this is because the memo dictionary can't use the list parameter as a key!
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Base cases
        if amount == 0: return 0
        if amount < 0: return -1
        curMinCoins = inf
        viable = False # We need this variable because we can't just use -1 for curMinCoins, or 
        # setting a new min won't work
        for coinVal in coins: # O(len(coins)^amount!!)
            curChange = 1 + self.coinChange(coins, amount-coinVal)
            if curChange>0 and curChange<curMinCoins:
                curMinCoins = curChange
                viable = True

        return curMinCoins if viable else -1

# Bottom up dp (tabulation)
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int: # O(amount*len(coins)) time, O(amount) space
        # Our dp array stores the minimum number of coins needed to make change for each amount,
        # corresponding to the index in the array.
        # When initialized, all values are set to amount+1, which is a value that is impossible to reach;
        # This is because the smallest coin val is 1, so we will need at most amount coins to make change.
        # The array is of length amount+1 because we want to include an entry for index amount and index 0,
        # if only amount entries then the last one would be amount-1
        dp = [amount + 1] * (amount+1) # O(amount)
        dp[0] = 0 # If amount is 0, then 0 coins are needed (base case)

        # Fill dp array bottom up
        for amt in range(1, amount + 1): # O(amount)
            # For each coin val, update dp[amt] if we can get a better solution by starting with that coin
            # and using the solution for the remaining amount
            for coinVal in coins: # O(len(coins))
                if amt-coinVal >= 0: # If we can't get exact change, it doesn't matter
                    dp[amt] = min(
                        1 + dp[amt-coinVal], # Using stored solution
                        dp[amt]              # Using current solution
                    )

        # If dp[amount] is still amount+1, then we never found a solution
        return dp[amount] if dp[amount] < amount+1 else -1


# Same as S1, but with a sliding window (not like the typical algorithm) to save space
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int: # O(amount*len(coins)) time, O(max(coins)) space
        dp = [0] # We start with just dp[0]=0, and we add to the array as we go

        for amt in range (1, amount+1):
            newVal = amount + 1
            for coinVal in coins:
                if amt-coinVal >= 0:
                    newVal = min(
                        1 + dp[-coinVal],
                        newVal
                    )
            if len(dp)==max(coins): dp.pop(0) # the optimization, since we only access as far back as -coinVal
            dp.append(newVal)

        return dp[-1] if dp[-1] < amount+1 else -1

# Note further optimization of this problem by usng combinations of solutions in some sort of tree?
# see https://en.wikipedia.org/wiki/Change-making_problem#Dynamic_programming_with_the_probabilistic_convolution_tree