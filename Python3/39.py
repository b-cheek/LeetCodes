# Combination Sum

# My attempt at tabulation. I couldn't figure out how to remove duplicates,
# so I gave up and used sorting to remove duplicate combinations.
class Solution0: # Probably wrong, but O(target * len(candidates) * len(candidates) * log(len(candidates)) time, O(target * len(candidates) * len(candidates)) space?
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for t in range(1, target + 1): # O(target)
            for num in candidates: # O(len(candidates))
                if num == t:
                    dp[t].append([num])
                elif t-num > 0 and dp[t-num]:
                    for arr in dp[t-num]:
                        dp[t].append(
                            arr + [num]
                        )

        res = []
        for arr in dp[target]: # I think O(target * len(candidates) * len(candidates) * log(len(candidates))?
            arr = sorted(arr)
            if arr not in res:
                res.append(arr)

        return res


# This solution uses DFS with backtracking, a form of DP.
# The idea is that for each candidate, you create 2 branches:
# One that includes the candidate, and one that does not.
# This is complicated since duplicate candidates are allowed,
# so the first branch is allowed to use the current candidate again,
# while the second branch is not.
# This way, each combination found will be unique
class Solution1: # Not gonna sweat the complexity. Something in the avenue of O(2^n) time, O(longest combination length) space
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # i is the current candidate, cur is the current combination, total is sum(cur)
        def dfs(i, cur, total):
            if total==target: # If the current combination sums to the target, add it to the result
                res.append(cur.copy()) # Since we continue to use cur, a list (which is mutable), 
                return                 # we need to add a DEEP copy to the result
            if i >= len(candidates) or total > target:
                return # if there are no more candidates to add or we exceed the target, return

            # 1st branch:
            cur.append(candidates[i]) # add the current candidate to the combination
            dfs(i, cur, total + candidates[i]) # recurse with the same candidate, since it can be used again
            # 2nd branch:
            cur.pop() # Remove candidates[i] from the combination
            dfs(i + 1, cur, total) # recurse with the next candidate, since candidate[i] cannot be used again

        dfs(0, [], 0) # Start the recursion with the first candidate, an empty combination, and a total of 0
                      # This recursively iterates through the candidates, adding solutions to res
        return res