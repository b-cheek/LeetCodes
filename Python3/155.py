# Min Stack

# This solution keeps track of the local minimums in a separate stack.
class MinStack0:

    def __init__(self):
        self.stack = deque([])
        self.min_stack = deque([]) # min_stack[-1] is the current minimum

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Check if the new value is the new minimum, as long as the stack exists.
        # I think the >= is necessary so we know when to pop the min_stack.
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        # If we are popping the current min, remove it from min_stack as well
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# This solution differs in that the min_stack is the same size as the stack.
# This means that each value in stack corresponds to the current minimum in min_stack.
# This removes the need to check if the value being removed is the current minimum.
# This tradeoff means the pop operation is faster, but the min_stack takes up more space.
class MinStack1:

    def __init__(self):
        self.stack = deque([])
        self.min_stack = deque([])

    def push(self, val: int) -> None:
        self.stack.append(val)
        # append current minimum to min_stack
        self.min_stack.append(
            min(self.min_stack[-1] if self.min_stack else val, val)
        )

    # Since the min_stack corresponds to the stack, we can just pop both.
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# This solution applies the same technique as the previous solution,
# but only uses a single stack.
# This is accomplished by storing the current minimum alongside each value in a tuple
class MinStack2:

    def __init__(self):
        # Stack of tuples, where tuple[0] is value, and tuple[1] is current minimum
        self.stack = deque([])

    def push(self, val: int) -> None:
        if not self.stack: 
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(
                val, self.stack[-1][1]
            )))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()