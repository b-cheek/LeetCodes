from collections import defaultdict
import heapq

class Solution0:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = defaultdict(int)
        for num in nums:
            frequencyDict[num] += 1

        temp = []
        for key in frequencyDict:
            temp.append((frequencyDict[key], key))

        return [sorted(temp, reverse=True)[i][1] for i in range(0,k)]

from collections import defaultdict

class Solution1: ## Bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = defaultdict(int)
        for num in nums:
            frequencyDict[num] += 1

        freq = [[] for i in range(0, len(nums)+1)] ## Nums + 1 since the index is freq, index is len - 1, so make them equal q=with len+1

        for num, count in frequencyDict.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            res += freq[i]
            if len(res)==k: return res
            ## Since answer is unique, equivalent works

class Solution2: ## Heap/Priority Queue
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = defaultdict(int)
        for num in nums:
            frequencyDict[num] += 1

        heap = []
        for key in frequencyDict:
            ## Add tuple of (-count, num) to heap
            heapq.heappush(heap, (-frequencyDict[key], key))
            ## Since min heap, you need to use negative to put highest freq at top

        res = []
        for i in range(0, k):
            res.append(heapq.heappop(heap)[1]) ## Get just the num with highest freq

        return res


## Note that another possible solution similar to S2 is to use a self balancing tree
## I saw this as an ordered map in java, actually a red black tree