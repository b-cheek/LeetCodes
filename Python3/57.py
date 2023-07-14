# Insert Interval

# I like the way this is broken into three cases and iterates through whole list.
class Solution0: # O(n) time, O(n) space
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # Handle intervals fully before newInterval (add to res)
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # Handle interval fully after newInterval (return res with rest of intervals)
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # Handle intervals overlapping newInterval (merge with newInterval)
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        
        # Handle the case where newInterval is the last interval in res
        res.append(newInterval)
        return res

# For some reason LC says this has same time complexity as above, even though no res list. 
# This is also is very similar to the above, so why use res? Maybe it is same space comp. and I'm missing something.
class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals):
            # Handle intervals fully before newInterval (add to res)
            if intervals[i][1] < newInterval[0]:
                i += 1

            # Handle interval fully after newInterval (return res with rest of intervals)
            elif intervals[i][0] > newInterval[1]:
                intervals.insert(i, newInterval)
                return intervals
            
            # Handle intervals overlapping newInterval (merge with newInterval)
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
                intervals.pop(i)
        
        # Handle the case where newInterval is the last interval in res
        intervals.append(newInterval)
        return intervals

s = Solution()

print(s.insert([[1,2]], [3,4]))