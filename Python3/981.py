# Time Based Key-Value Store

class TimeMap0:

    def __init__(self):
        self.timeMap = [] # A list of tuples containing two items:
                          # The timestamp, and a dictionary

    def set(self, key: str, value: str, timestamp: int) -> None: # O(1)

        if self.timeMap and timestamp == self.timeMap[-1][0]:
            timeMap[i][1][key] = value
            
        else: self.timeMap.append((timestamp, {key: value}))
        
    def get(self, key: str, timestamp: int) -> str: # O(n), could be improved with bin search
        for i in range(len(self.timeMap)-1, -1, -1):
            if self.timeMap[i][0] <= timestamp and key in self.timeMap[i][1]:
                return self.timeMap[i][1][key]
        return ""
        

# Note that python dicionaries preserve insertion order as of python 3.7, so we could use a dictionary of dictionaries
# I don't want to waste time thinking about implementation, but you'd have to use iterators or .keys() or .items() perhaps.

class TimeMap1:

    def __init__(self):
        self.timeMap = dict() # A dictionary of lists, where each list contains
                              # tuples with the timestamp and the value, ordered by timestamp

    def set(self, key: str, value: str, timestamp: int) -> None: # O(1)

        # Could use defaultdict to avoid this
        if key in self.timeMap:
            self.timeMap[key].append((timestamp, value))

        else:
            self.timeMap[key] = [(timestamp, value)]
        
    def get(self, key: str, timestamp: int) -> str: # O(n), could be improved with bin search
        if key in self.timeMap:
            keyHistory = self.timeMap[key]
            for i in range(len(keyHistory)-1, -1, -1):
                if keyHistory[i][0] <= timestamp:
                    return keyHistory[i][1]
        return ""
        

# This solution implements defaultdict and bin search as mentioned above. (ends up taking more memory anyway)
class TimeMap(object):

    def __init__(self):
        self.timeMap = collections.defaultdict(list) # Dictionary of lists like above
                                                     # default to empty list if key doesn't exist

    def set(self, key, value, timestamp):
        self.timeMap[key].append([timestamp, value]) # Defaultdict takes care of the case where key doesn't exist

    def get(self, key, timestamp):
        keyHistory = self.timeMap[key]
        
        # Doing bin search implementations make me want to use stl functions :(
        left = 0
        right = len(keyHistory) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if keyHistory[mid][0] < timestamp:
                left = mid + 1
            elif keyHistory[mid][0] > timestamp:
                right = mid - 1
            else:
                return keyHistory[mid][1] # If we find the exact timestamp, return the value

        # Need a little more logic for bin search, but not bad
        return "" if not keyHistory or keyHistory[right][0] > timestamp \
                  else keyHistory[right][1]

        # A brif explainer on the above to help understanding:
        # I could have checked if the key is in the dict, but I like having the not keyhistory check with other checks.
        # keyHistory[right][0] > timestamp means that the timestamp is smaller than the smallest timestamp in the list (note right < left at end)
        # Otherwise, return keyHistory[right][1]. This is the value at the first timestamp smaller than target, I think for the above ^ reason?

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
