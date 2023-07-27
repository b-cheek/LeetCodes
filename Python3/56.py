# Merge Intervals

# This solution sorts the intervals, and then iterates through intervals 
# while updating an output array "res" by either
#   merging the interval with the last interval in res if overlap or
#   adding the interval if no overlap
class Solution0:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0]) # Sort by the start position of the interval
        res = [intervals[0]] # We know that the first interval must be in the result, since it has leftmost start
        for i in range(1, len(intervals)): # Note that I should have used destructuring here to simplify nested lists
            if intervals[i][0] <= res[-1][1]: # If overlapping
                # Left end is set because sort order, right end is set to max of both
                res[-1][1] = max(res[-1][1], intervals[i][1]) # I could just store the end of the previous interval
            else:
                res.append(intervals[i])

        return res


# Same as S0, but modifying intervals in place
class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        i = 1
        # Different than S0 in that we use while since we are changing the sequence being iterated in S0.
        # We keep i to track index; note that popping i moves intervals[i] to the next interval,
        # so only increment i if we aren't popping.
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1

        return intervals


# Same as S1 except we go backwards, 
# which results in having to shift fewer elements overall for each pop.
# Logically the exact same but mirrored, so sort by interval[1],
# iterate backward, use min(), switch start vs end in comparisons.
class Solution2: # BEST SOLUTION IMO, O(nlogn) time, no aux space
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[1])
        i = len(intervals) - 2
        while i >= 0:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = min(intervals[i+1][0], intervals[i][0])
                intervals.pop(i)
            i -= 1

        return intervals


# Note that this question is solved in O(n^2) time if you can't use sorting
# by transforming the list of intervals into a graph (adjacency list),
# Where overlapping intervals are connected nodes.
# Use dfs to identify connected components, and create a merged interval for each,
# and return a list with the interval representing each connected component.
# This is also O(n^2) space, since each interval in graph could overlap all other intervals.