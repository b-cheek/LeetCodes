class Solution0: #Basic implementation, in place
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range (len(nums)): nums[i]**=2
        nums.sort()
        return nums

class Solution1: #Not really a fast and slow pointer solution, just 2 pointer
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0]>=0 or len(nums)<2: #If all positive or only one value, you can just square
            for i in range(len(nums)):
                nums[i]**=2
            return nums
        
        fast = 1 #Since first element must be <0
        while fast<len(nums) and nums[fast]<0:
            fast += 1 #increment fast until it is at the first non-negative element
        slow = fast-1 #slow is the last negative element

        #Slow and fast will be at the switch from negative to non-negative respectively
        #They will check to see which absolute value is less, add it's square to the new array, and move the pointer to the next (greater abs val) element

        newArr = []
        while True:
            if slow<0: #end condition to finish if slow reaches edge first (I think the semi-sorted order makes such an end condition optional)
                while fast<len(nums):
                    newArr.append(nums[fast]**2)
                    fast+=1
                return newArr
            if fast>=len(nums): #end condition to finish if fast reaches edge first
                while slow>=0:
                    newArr.append(nums[slow]**2)
                    slow-=1
                return newArr
                
            if nums[slow] + nums[fast] > 0: #if abs(slow) < abs(fast)
                newArr.append(nums[slow]**2) #add its square
                slow -= 1 #move pointer towards edge
            else:
                newArr.append(nums[fast]**2)
                fast += 1

class Solution2: #I guess this is how you do functional programming in python
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums]) #Note that this is not in place, so uses some auxiliary space

class Solution3: #Adapted rom https://leetcode.com/problems/squares-of-a-sorted-array/discuss/310865/Python%3A-A-comparison-of-lots-of-approaches!-Sorting-two-pointers-deque-iterator-generator
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return_array = [0] * len(nums)
        left_read_pointer = 0
        right_read_pointer = len(nums) - 1
        left_square = nums[left_read_pointer] ** 2
        right_square = nums[right_read_pointer] ** 2
        for write_pointer in range(len(nums)-1, -1, -1): #since the return array will be backwards, the pointer starts at the end and moves backwards until return_array is full
            if left_square > right_square:
                return_array[write_pointer] = left_square
                left_read_pointer += 1
                left_square = nums[left_read_pointer] ** 2
            else:
                return_array[write_pointer] = right_square
                right_read_pointer -= 1
                right_square = nums[right_read_pointer] ** 2
        return return_array

from collections import deque
class Solution3: #Adapted from https://leetcode.com/problems/squares-of-a-sorted-array/discuss/310865/Python%3A-A-comparison-of-lots-of-approaches!-Sorting-two-pointers-deque-iterator-generator
    def sortedSquares(self, nums: List[int]) -> List[int]:
        number_deque = deque(nums) #Deque actually feels very well suited for this problem
        reverse_sorted_squares = []
        while number_deque:
            if number_deque[-1] + number_deque[0] < 0: #Needs peeking
                reverse_sorted_squares.append(number_deque.popleft()**2) #appends while also popping
            else:
                reverse_sorted_squares.append(number_deque.pop()**2)
        return reverse_sorted_squares[::-1]

#From https://leetcode.com/problems/squares-of-a-sorted-array/discuss/310865/Python%3A-A-comparison-of-lots-of-approaches!-Sorting-two-pointers-deque-iterator-generator
class SquaresIterator(object): #If you haven't checked recently, get a refresher on iterators
    def __init__(self, sorted_array):
        self.sorted_array = sorted_array
        self.left_pointer = 0
        self.right_pointer = len(sorted_array) - 1
    
    def __iter__(self): #Returns the iterator itself, kind of like initializing the iteration
        return self
    
    def __next__(self): #Returns next element of the iterable object
        if self.left_pointer > self.right_pointer: #stops iterating at the right time
            raise StopIteration
        left_square = self.sorted_array[self.left_pointer] ** 2
        right_square = self.sorted_array[self.right_pointer] ** 2
        if left_square > right_square:
            self.left_pointer += 1
            return left_square
        else:
            self.right_pointer -= 1
            return right_square  

class Solution4:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return_array = [0] * len(nums)
        write_pointer = len(nums) - 1
        for square in SquaresIterator(nums): #For loop demonstrates how this iterator is like how a list is an iterator
            return_array[write_pointer] = square
            write_pointer -= 1
        return return_array


#From https://leetcode.com/problems/squares-of-a-sorted-array/discuss/310865/Python%3A-A-comparison-of-lots-of-approaches!-Sorting-two-pointers-deque-iterator-generator
class SquaresIterator(object):
    
    def __init__(self, sorted_array):
        self.sorted_array = sorted_array
        self.left_pointer, self.right_pointer = self._get_pointers() #This version puts pointers in the middle like my OG solution so the list is in order from the iterator
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        # If there's no values remaining.
        if self.left_pointer < 0 and self.right_pointer >= len(self.sorted_array):
            raise StopIteration
        
        # If there's no values remaining on the left end.
        if self.left_pointer < 0:
            self.right_pointer += 1
            return self.sorted_array[self.right_pointer - 1] ** 2
        
        # If there's no values remaining on the right end.
        if self.right_pointer >= len(self.sorted_array):
            self.left_pointer -= 1
            return self.sorted_array[self.left_pointer + 1] ** 2
        
        # If there's values remaining on both ends.
        left_square = self.sorted_array[self.left_pointer] ** 2
        right_square = self.sorted_array[self.right_pointer] ** 2
        if left_square < right_square:
            self.left_pointer -= 1
            return left_square
        else:
            self.right_pointer += 1
            return right_square
    
    
    def _get_pointers(self): #Binary search to put the pointers in the middle
        low = 0
        high = len(self.sorted_array)
        while high - low > 1: #Stops when the pointers meet each other in the middle, cool version of binary search
            mid = low + (high - low) // 2
            if self.sorted_array[mid] > 0:
                high = mid
            else:
                low = mid
        return low, high
        
    
class Solution5:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return list(SquaresIterator(nums)) #No need for reversal


#From https://leetcode.com/problems/squares-of-a-sorted-array/discuss/310865/Python%3A-A-comparison-of-lots-of-approaches!-Sorting-two-pointers-deque-iterator-generator
class Solution6:
    
    def generate_sorted_squares(self, nums): #Generator function
        
        # Start by doing our binary search to find where
        # to place the pointers.
        left = 0
        right = len(nums)
        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                right = mid
            else:
                left = mid
        
        # And now the main generator loop. The (while loop) condition is the negation
        # of the StopIteration condition for the iterator approach.
        while left >= 0 or right < len(nums):
            if left < 0:
                right += 1
                yield nums[right - 1] ** 2 #yield returns a value, but allows the while loop to continue if revisited
            elif right >= len(nums):
                left -= 1
                yield nums[left + 1] ** 2 #also note the adding must be done so the loop can decrement/increment the respective pointer before yielding which stops the loop (temporarily)
            else:
                left_square = nums[left] ** 2
                right_square = nums[right] ** 2
                if left_square < right_square:
                    left -= 1
                    yield left_square
                else:
                    right += 1
                    yield right_square
        
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return list(self.generate_sorted_squares(nums))