# Evaluate Reverse Polish Notation

from collections import deque

# The idea with this solution comes from the fact that RPN just takes the last two things,
# can be basic operand or an expression. To solve this, I put stuff on a stack, and if an
# operator shows up, replace the last two operands with their computed value.
# Kinda surprised I got this
class Solution0:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens: # Add every token to the stack, computing expressions as you go
            try: # If the token is a number, add it's value to the stack
                stack.append(int(token))
            except: # Otherwise, compute the value of the expression
                operands = stack.pop(), stack.pop() # Destructuring
                if token == '+':
                    # Note that order is 1, 0 since the left operator is popped second
                    stack.append(operands[1] + operands[0])
                elif token == '-':
                    stack.append(operands[1] - operands[0])
                elif token == '*':
                    stack.append(operands[1] * operands[0])
                else:
                    stack.append(int(operands[1] / operands[0])) # This truncates to 0

        return stack.pop() # The remaining value in the stack represents the computed solution of the entire expression

# Remove try except for efficiency
# The annoying part about that is that it makes setting up the operands weirder.
# Since there isn't another simple catch-all way to check if integer, we do that as
# the else condition. This means though that we can't set the operands until we know the token is an operator,
# so we need to repeat each time. 
class Solution1:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token == '+':
                operands = stack.pop(), stack.pop()
                stack.append(operands[1] + operands[0])
            elif token == '-':
                operands = stack.pop(), stack.pop()
                stack.append(operands[1] - operands[0])
            elif token == '*':
                operands = stack.pop(), stack.pop()
                stack.append(operands[1] * operands[0])
            elif token == '/':
                operands = stack.pop(), stack.pop()
                stack.append(int(operands[1] / operands[0]))
            else:
                stack.append(int(token))
                
        return stack.pop()


# Solve problem in S1 by creating a map of operators to the functions they represent
# Could also do the popping in the map, but I think this way is more readable
class Solution2:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operations = {
            '+': lambda l, r: l + r,
            '-': lambda l, r: l - r,
            '*': lambda l, r: l * r,
            '/': lambda l, r: int(l / r)
        }
        
        for token in tokens:
            if token in operations:
                r, l = stack.pop(), stack.pop() # More readable than destructuring imo, note still backwards
                stack.append(operations[token](l, r)) # Evaluate with the appropriate function and add to stack
            else: 
                stack.append(int(token))

        return stack.pop()