# This implementation will retain queue order in the items member
class MyQueue0:

    def __init__(self):
        self.items = deque()
        self.temp = deque()

    # Whenever you push, empty the items into the temp, push the new item into the items, then empty the temp back into the items to retain q order
    def push(self, x: int) -> None: # O(2n)
        while self.items:
            self.temp.append(self.items.pop())
        self.items.append(x)
        while self.temp:
            self.items.append(self.temp.pop())

    def pop(self) -> int: # O(1)
        return self.items.pop()

    def peek(self) -> int: # O(1) 
        return self.items[-1]

    def empty(self) -> bool:
        return len(self.items)==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# This version is like the above;
# The difference is that you "flip" for both operations.
# "Flip" will be used to describe the process of emptying one stack into another, "flipping" the stack upside down
# You can apply the same logic from S0 for both ways, but I think the simpler explanation is that:
# A queue is defined by pushing on the opposite side from where you pop;
# To accomplish this with a stack, just flip it over each time you switch operations
class MyQueue1:

    def __init__(self):
        self.pushStack = deque()
        self.popStack = deque()

    def push(self, x: int) -> None: # O(n) worst case, O(1) amortized
        if self.popStack: # Flip if the last operation was a pop
            while self.popStack:
                self.pushStack.append(self.popStack.pop())

        self.pushStack.append(x)

    def pop(self) -> int: # O(n) worst case, O(1) amortized
        if self.pushStack: # Flip if the last operation was a push
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
                
        return self.popStack.pop()

    def peek(self) -> int: # O(n) worst case, O(1) amortized
        if self.pushStack: # Flip if last operation was a push
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
            
        return self.popStack[-1]

    def empty(self) -> bool:
        return len(self.pushStack)==0 and len(self.popStack)==0 # Now either one or the other stacks will contain all the items at a time

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# This solution improves upon the last by only flipping the push (input) stack
# Since queue is FIFO, that means we only need to access the input stack once the output stack (queue) is empty
# The way this works is that any time we run out of output, we flip the input stack into the output stack
# Then we can continue to pop in queue order, and new items pushed to the input won't be needed until the output is empty again
class MyQueue2:

    def __init__(self):
        self.input = deque()
        self.output = deque()

    def refill_if_empty(self): # check if output is empty; if so, flip input into output (O(n) worst case, O(1) amortized)
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

    def push(self, x: int) -> None: # O(1)
        self.input.append(x)

    def pop(self) -> int: # O(n) worst case, O(1) amortized
        self.refill_if_empty()      
        return self.output.pop()

    def peek(self) -> int: # O(n) worst case, O(1) amortized
        self.refill_if_empty()
        return self.output[-1]

    def empty(self) -> bool:
        return len(self.input)==0 and len(self.output)==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()