# DSA Dictionary

Note I am only adding to this document AS I COME ACROSS things that I don't know.

## Data Types

### List

Collection that is

* Ordered
* Mutable
* Allows duplicates

**Initialize:**

```python
myList = [1, 2, 3]
myList = ['a', 'b', 'c']
myList = [0]*26
myDigitsList = [i for i in range(10)] # List comprehension
```

Note that the 2nd to last list is initialized with 26 0's.
Only use this technique for immutable values, otherwise you will create shallow copies of the same object. For example, `[[]]*26` will fill the parent list with 26 references to the same list object!

note that `list()` is a constructor to return a list

in LC problems you will often see

```python
nums: List[int]
```

This is stricly used for typing (defining a type like in a statically typed language), and requires `from typing import list`

**Remove:**

```python
myList.pop(index) # Removes item at index from list, defaults to last item, returns value
myList.remove(item) # Removes first occurrence of item, no return
```

**Append:**

```python
temp = [1,2]
temp.append(3)
temp == [1,2,3]
```

Also see the List section of [Concatenation](#concatenate)

### String

Note that strings are like arrays. However, there is no character data type, just strings of length 1.

**Initialize:**

```python
myStr = "Hello World!"
smallStr = 'a'
```

Again note that `smallStr` is just a str of length 1, also illustrating that there is no difference between single and double quotes, I just like to use single quotes for small things like that as a matter of convention.

**Append:**

```python
msg = "Hello"
msg += " world!"
msg == "Hello World!"
```

Note that + can also be used for [concatenation](#concatenate)

**Replace/Remove:**

```python
string.replace('oldVal', 'newVal', count=0)
```

Count optionally specifies the number of occurrences to replace. To use `replace` to remove, you can just do `myString.replace('removeVal', '', 1)`. Note that this will do nothing if `removeVal` is not present, so if you need to know if the substring was present or not you should convert to a list and use the remove method from [list](#list)

**To Lowercase:** `myStr.lower()` (Note this returns a string, not in place)

**Check if alphanumeric:** `myStr.isalnum()`

**Check if number:**

```python
# Difference in unicode classification
myStr.isdecimal()
myStr.isdigit()
myStr.isnumeric()
# isnumeric includes the most unicode characters,
# but NONE OF THESE work for negative or decimals

# Works with negative and decimals. Note behavior of int()
try:
  # If numeric
  int(myStr)
except:
  # If not numeric
```

[Difference between is...() functions](https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-pyth)

[Behavior of int()](#truncation-towards-zero)

**Regex:**

```python
import re

def is_number(input_str): # Match for a +/- int or float
    pattern = r'^[-+]?\d*\.?\d+$'
    return re.match(pattern, input_str, re.ASCII) is not None
```

Here is a breakdown of this expression so you can modify it for your own use:

* `^`: Matches the start of the string.
* `[-+]?`: Matches an optional positive or negative sign.
* `\d*`: Matches zero or more digits
* `\.?`: Matches an optional decimal point.
* `\d+`: Matches one or more digits.
* `$`: Matches the end of the string.
* `re.ASCII`: A flag changes the default from full unicode matching to ASCII matching (`/d == [0-9]`)

#### Formatting

fstrings allow you to insert variables into your strings easily:

```python
age = 20
ageString = f"I am {age} years old"
ageString == "I am 20 years old"
```

### Set

Collection that is

* Unordered
* Mutable
* No duplicates

**Initialize:**

```python
mySet = {"apple", "banana", "cherry"}
emptySet = set()
```

Check if contains: `if "apple" in mySet`

**Append:** `mySet.add(3)`
**Remove:** `mySet.remove(3)`

### Tuple

Collection that is

* Ordered
* Immutable
* Allows duplicates

**Initialize:**

```python
myTuple = (1, 2, 3)
otherTuple = 1, 2, 3
myTuple==otherTuple
```

Note that initializing a tuple without parentheses and unpacking its contents into other variables is often used for assignment patterns, see [Sequence Unpacking](#sequence-unpacking)

**Access:**

```python
myTuple = ('a', 'b', 'c')
myTuple[1]=='b'
```

### Dictionary

Collection (of key-value pairs) that is:

* Ordered (unordered until Python 3.7)
* Mutable
* Duplicate (keys) not allowed

**Initialize:**

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
emptyDict = {}
```

**Append:**

```python
myDict = {1: "One"}
myDict[2] = "Two"
myDict == {
  1: "One",
  2: "Two"
}
```

**Access:**

`thisdict["brand"] == "Ford"`

OR

```python
thisdict.get("brand", None) == "Ford"
```

Note that the `None` can be replaced with a default value. See example usage below after defaultdict

but will return `None` if there is no brand key.

NOTE: anything that is immutable can be used as a key. This means that strings and tuples are viable, but not lists, sets, or dicts.

NOTE the existence of defaultdict:

```python
from collections import defaultdict

myDefaultDict = defaultdict(list)
## Currently empty
myDefaultDict["nonExistentKey"].append(["wow"])
```

The above code shows how default dict will initialize a key to an empty default type if not already present. Pretty helpful huh

Alternatively, you can use .get, which takes an argument to return a default value if there is no key:

```python
dict.get(keyname, value)
## In our example:
myDict = {}
## Currently empty
myDict["nonExistentKey"] = 
  myDict.get("nonExistentKey", []) += [["wow"]] 
  ## Note that double brackets are necessary because      concatenating not appending
```

**Iterate:**

```python
for key in myDict:
  print(myDict[key])

for value in myDict.values():
  print (myDict[value])

for key, value in myDict.items():
  print("Key:", key)
  print("Value:", value)
```

### Priority Queue (Heap)

**Initialize:**

```python
import heapq

myHeap = []
```

Note that this is just a list. A heap is often represented as a list, read up on heaps. The heapq module (likely named because a heap is teh typical implementation of a priority queue) gives methods to perform heap operations on a list.

**Append:**

`heapq.heappush(myHeap, item)`

Note that `item` can be anything I think, I don't know if there is a way to modify the invariant though

**Access/Remove:**

`heapq.heappop(myHeap)`

Note that this will pop the item with the smallest value from the heap, since heapq does a min heap.

**Push and Pop at the same time!**

`heapq.heappushpop(myHeap, item)`

This is useful to maintain a certain size heap

### Stack/Queue (Deque)

Stacks and queues are typically implemented using python's deque (pronounced "deque") module, short for double-ended queue. This means that you can pop or push from either the left or right end

**Initialize:**

```python
from collections import deque

myDeque = deque()
myDeque = deque([1,2,3])
```

**Check if empty:**

```python
if len(dq)==0:
if not len(dq):
```

Note in the following sections that the push vs pop for stack vs queue is technically arbitrary.

For stack, pop from the same side you push, and for queue, pop from the opposite side you push. I just have the following preferences:

#### As a Stack

**Push:** `myStack.append(1)`

**Pop:** `myStack.pop()` (Note this returns the popped value as well)

**Peek:** `frontVal = myStack[-1]`

#### As a Queue

**Push:** `myQ.append(1)`

**Pop:** `myQ.popleft()`

**Peek:** `myQ[0]`

### Counter

> A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts

\- [Python Docs](https://docs.python.org/3/library/collections.html#collections.Counter)

**Initialize:**

```python
from collections import Counter

c = Counter() # a new, empty counter
c = Counter('gallahad') # a new counter from an iterable (this will track the number of occurrences for each character)
c = Counter({'red': 4, 'blue': 2}) # a new counter from a mapping
c = Counter(cats=4, dogs=8) # a new counter from keyword args
```

Note that counters support various math and logic operations, such as subtraction in [P383.3](/Python3/383.py)

### Lambda

```python
lambda arguments : expression
```

Here is a simple example making a multiplication function with `def`, and then the same function with `lambda`

```python
def multiply(a, b):
  return a*b

lambdaMultiply = lambda a, b : a*b
```

I also like this example from [W3Schools](https://www.w3schools.com/python/python_lambda.asp):

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
```

Note that a lambda can be used as an argument for a function (like in [sort](#sort) and [filter](#filter)), as a value in a hash map (see [P150.2](/Python3/150.py)), etc.

### Object (Class)

I think its best to explain class with an example of a class:

```python
class Dog:

  legs = 4 # Class variable

  def __init__(self, breed): # Constructor
    self.breed = breed

  def __str__(self): # when you use built-in str() fn
    return f"I am a {self.breed}"

  def recurse(self):
    return self.recurse()

Rodger = Dog("pug")
Dog.legs == 4
Rodger.legs == 4
Rodger.breed == "pug"
```

## Algorithms

### Max/Min

```python
myList = [1,2,3]

max(myList) == 3
max(1,2,3) == 3

min(myList) == 1
min(1,2,3) == 1
```

### Truncation

The practice of removing decimal points

#### Floor

```python
from math import floor
floor(1.7)==1
```

Note that floor is commonly used with division, such as in finding a midpoint for binary search ([P704](/Python3/704.py))

In this case, you can use the integer division operator: `3//2==1`

#### Ceiling

```python
from math import ceil
ceil(-1.7)==-1
```

#### Truncation towards zero

```python
int(-1.7)==-1
int(1.7)==1
```

Note that this technique strictly just removes any decimal value, whereas `floor` and `ceil` will round down or up respectively. I guess this is helpful if you're thinking of the int as a vector, so this just truncates the magnitude no matter the direction. Note that this technique is used with division in [P150](/Python3/150.py).

### Modulus (%)

Modulus returns the remainder of a division operation, but python notably does it different than other languages like C++ and java.

C++ and Java use *truncated division*, where the remainder has the same sign as the dividend

Python uses *floored division*, where the remainder has the same sign as the divisor.

This causes different behavior in a modulus expression with exactly one negative operand:

in Python:

```python
(-5) / 4 = -1.25 --> floor(-1.25) = -2
(-5) % 4 = (-2 × 4 + 3) % 4 = 3
```

in C++/Java:

```java
(-5) / 4 = -1.25 --> trunc(-1.25) = -1
(-5) % 4 = (-1 × 4 + -1) % 4 = -1
```

You can replicate the C++/Java behavior in python by using `math.fmod(divisor, dividend`.

### Absolute value

```python
abs(-1)==1
```

Built in function, no keywords necessary.

### Deep copy

Whenever using a mutable data type, the variable is simply a pointer to the data. This means that if you assign a variable to another variable, they will both point to the same data. This is called a shallow copy. A deep copy is when you copy the data itself, so that the two variables point to different data.

Most commonly, you need to make a deep copy of a `List` (note that unlike other langauges, strings in python are immutable):

```python
myList = [1,2,3]
myCopy = myList.copy()
unpackCopy = [*myList]
sliceCopy = myList[:] # maybe fastest?
listCopy = list(myList)
listCompCopy = [i for i in myList]
```

See how the last one is necessary in the [List](#list) initialization section.

### Sort

Note that python uses [Timsort](https://en.wikipedia.org/wiki/Timsort#), which is stable and O(nlogn) time, O(n) space (better with semi-ordered data)

**Any iterable:**

```python
sorted(iterable, key=key, reverse=reverse)
```

Returns sorted iterable

[W3 page](https://www.w3schools.com/python/ref_func_sorted.asp)

**Lists:**

```python
list.sort(reverse=True|False, key=myFunc)
```

Modifies list in place

[W3 page](https://www.w3schools.com/python/ref_list_sort.asp)

#### Sort Key

To define the sorting order, use the key parameter, a function that returns the thing to be sorted by.

This example sorts a list of strings by (increasing) length instead of alphabetically:

```python
myStrList.sort(key=lambda s : len(s))
```

### Automatic Memoization with @cache

Automatically applies memoization in the cache to the following function.

The [Python Docs](https://docs.python.org/3/library/functools.html) explain it very well.

```python
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

>>> factorial(10)      # no previously cached result, makes 11 recursive calls
3628800
>>> factorial(5)       # just looks up cached value result
120
>>> factorial(12)      # makes two new recursive calls, the other 10 are cached
479001600
```

### Filter

```python
filter(function, iterable)
```

if the function returns True then it passes through the filter (the item remains in the iterable)

Note the existence of [lambdas](#lambda), useful for functions with function parameters

For example see this fragment adapted from [P125](/Python3/125.py):

```python
alNumIter = filter(lambda char : char.isalnum(), s)
```

Note that the filter function returns an iterator, use `''.join(alNumIter)` to turn it back into a string

### Lambda function

For general use, see the [explanation](#lambda) in the data types section.

Note that lambda functions are useful as parameters to other functions, see [sort](#sort) and [filter](#filter).

### Concatenate

**Strings:**

```python
part1 = 'py'
part2 = 'thon'
myStr = part1 + part2
print(myStr)
```

`python`

Works generally how you think, with += as well, etc.

**Lists:**

```python
[1,2,3] + [4,5,6] == [1,2,3,4,5,6]
myNums = [1,2,3]
myNums.extend([4,5,6]) # Or myNums += [4,5,6]
myNums == [1,2,3,4,5,6]
```

String items of an iterable: (The items **MUST** be strings)

```python
"separator".join(iterable)
```

The separator is a **required** string, do `''.join()` to join without separator.

Example:

```python
myTuple = ("John", "Peter", "Vicky")
x = '#'.join(myTuple)
print(x)
```

`John#Peter#Vicky#`

### Slicing/Subscripting

A lot of the following is taken from this [GREAT stackoverflow post
](https://stackoverflow.com/questions/509211/how-slicing-in-python-works)

I typically think of this as being used to access ordered iterables, like lists, strings, tuples, etc.

```python
[start=0:stop:step=1] ## Note that "stop" is the first value NOT in the slice
## To exlude paramaters, keep colons
## For example,
myReverseStr = myStr[::-1]
myDeepCopy = myList[:] ## Note that deep copy is irrelevant to strings since they are immutable, don't need to worry about that
```

Note that this also is obviously used to access items and not just return a sublist, for example:

```python
firstItem = myList[0]
lastItem = myList[-1]
```

But I guess that doesn't really follow the parameters of using the subscript operator (`[]`) to slice.

Speaking of slicing, there's a whole function that does the same thing.

```python
myList[2:6] == myList[slice(2, 6)]
```

### Rotate a list (No algorithm, alternatives)

There is no algorithm to rotate a list, but the suggested way to do it would be to call `pop()` and `append()` as necessary

```python
myList = [1,2,3]
temp = myList.pop(0)
myList.append(temp)
myList == [3,2,1]

# Or do it in one line if applicable:
myList.append(myList.pop(0))
myList == [2,1,3]
```

You can also add to the front of a list with `insert(0, item)` to rotate in the other direction.

### Sequence Unpacking

We can extract values from any iterable during assignment

```python
nums = [1, 2, 3]
num0, num1, num2 = myNums
left, right = 0, len(nums)-1 # Note that this is technically unpacking a tuple
myDict = {'a': 1, 'b': 2}
key0, key1 = myDict # Recall that iterating through a dict defaults to keys
```

See: [Tuple](#tuple): initialization and [dictionary](#dictionary): iteration

If you are assigning fewer variables than the length of the sequence being unpacked, use `*` to get the remainder of the elements

```python
fruits = ("apple", "banana", "strawberry", "cherry")
green, yellow, *red = fruits

green == 'apple'
yellow == 'banana'
red == ['strawberry', 'cherry']
```

My main use for this has been copying values of lists:

```python
myDeepCopy = [*myList]
myStrList = [*myString]
```

### Change Data Type

str to list: `myList = list(myStr)` or `myList = [*myStr]`

char to int: `myInt = ord(myChar)`

list to str: `myStr = str(myList)` (Note that the result looks like `"[1, 2, 3]"` as if in console)

list of strings to string: `myStr = ''.join(myStrList)`

list to tuple: `myTuple = tuple(myList)`

list to set (removes duplicates): mySet = `set(myList)`

float to int: `myInt = int(myFloat)` (Note that this will [truncate](#truncation-towards-zero) the result)

### Length

```python
len(object)
```

returns number of items in an object or characters in string

### Find

Often you want to check if a certain item exists in an iterable

```python
if key in myDict:
if item in myList
myList.index(item) # Returns first ocurrence of item, throws error otherwise
```

## Miscellaneous

### Comparison Chaining

In python you can chain comparisons. From [Python 3 Docs](https://docs.python.org/3/reference/expressions.html#comparisons)

> Comparisons can be chained arbitrarily, e.g., x < y <= z is equivalent to x < y and y <= z, except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).

See how this is applied in [P235](../Python3/235.py):

```python
p.val<root.val>q.val ## Both p and q have a val < root
p.val>root.val<q.val ## Both are greater
p.val<q.val<root.val ## See below
```

The last statement also implies p and q are less than root by the transitive property, but note that it explicitly says that p is less than q, which might be too specific.

### Infinity

```python
maxNum = float("inf")

## OR

from math import inf
maxNum = inf
```

### Max Int

The int type is unbounded, so max int will be same as the max word size for the interpreter, typically same as the system's max word size.

```python
import sys

sys.maxsize==9223372036854775807 # x64 systems, =2^63-1
sys.maxsize==2147483647 # x32 systems, =2^31-1
```

### Prevent Overflow

In a case where you are working with very large numbers, even though a result is < [maxsize](#max-int), an intermediate value could cause overflow. A great example is binary search([P704](/Python3/704.py)):

```python
l = 0
r = len(nums)-1
while l<=r:
    m = l+(r-l)//2 # Using this instead of (l+r)//2 prevents overflow
    if target<nums[m]:
        r = m-1
    elif target>nums[m]:
        l = m+1
    else:
        return m
return -1
```

### Error Handling (Try/Except)

```python
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
```

Note that this is helpful algorithmically for functions that return an error on certain conditions. For example, see how [P383.0](/Python3/383.py) uses a try/except block to remove an item from a list if it exists, otherwise returns False instead of throwing an error.

### Control flow

#### For loops

```python
for num in numsList:
  print(num)
```

Note that python technically only supports enhanced for loops like above, but you can always use a generator:

```python
for index in range(len(numsList)):
  print("Index:", index)
  print("Value:", numsList[index])
```

#### Enumerate (For loop with index and item)

Takes a collection and gives an id to each item, useful to get features of a traditional and enhanced for loop

```python
for index, value in enumerate(nums):
  print("The index is", index)
  print("The value is", value)
```

#### Range

Note that I pretty much only use `range()` in for loops, so this description will reflect that. Note that range actually returns a range object, but is as an iterable for my purposes

**Initialize:**

```python
range(start=0, stop, step=1)
```

Note that `start=0` and `step=1` indicates that these are optional parameters, and gives their default value.

**Keywords:**

`break`: break out of a for or while loop

`continue`: skip to the next iteration of a for or while loop

### Helper functions

I am doing this in the context of leetcode, so I'll give an example in their kind of format:

```python
class Solution:
  def algorithm(self, nums: List[int], target: int) -> int:
    def helper(target: int):
      # Do some recursive operation on nums
      return helper(target - 1)

    return helper(target)
```

This might be a little weird, but the point is to demonstrate how the helper function is just a part of `algorithm`. If the helper were another class member, then we could pass self (like `this` for the `Solution` object), but it's not necessary.

Note that if we are doing recursion without a helper function, we **will** use self, since it is a member of the solution class:

```python
class Solution:
  def recursiveAlgorithm(self, nums: List[int], target: int) -> int:
    # Do some recursive operation on nums
    return self.recurseiveAlgorithm(nums, target-1)
```

### Ternary operator

Python ternary operator is accomplished with `if` and `else` in the following fashion:

```python
value_if_true if condition else value_if_false
```

You can also conditionally execute expressions, so be creative.

### Assignment expressions / Walrus operator :=

Use the walrus operator to assigns values to variables as part of a larger expression.

```python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```

See it used in [P33](/Python3/33.py)

### Falsey coalescence / Short circuits / Elvis operator

Sometimes it is useful to return/use a value only if it is not falsey, and otherwise use some other value. This can be done using the logical or in python:

```python
myNums = [1, 0]
for num in myNums:
  print(num or "Zero")
# Prints:
# 1
# Zero
```

You can also use short circuiting to conditionally evaluate statements;

Lets say you have an expensive calculation, that you only want to perform if some condition is True, and has a default value if it returns a falsey value.

Typically you may do that like this:

```python
if perform_calculation:
  if (not result:=perform_expensive_calculation()):
    result = "Default Value"
```

Which is already somewhat sophisticated, using the [walrus operator](<keywordDict.md#Assignment expressions / Walrus operator :=>). Note how you could also make use of the ternary operator here. Alternatively, use short circuiting with logical AND OR

```python
result = perform_calculation \
  and perform_expensive_calculation() \
  or "Default Value"
```

Ther are some pretty creative ways to use short-circuiting, but this example is the most clear. Be creative! (but keep your code readable)

## Other concepts to understand

I think the best way to explain this section is to just explain why I decided to add it. In P347, I used the heapq module, and I think in an interview it's reasonable to expect an interviewer to check if I understand heaps in general. Since that knowledge isn't required to write the python code, I won't go into full detail since this is a "keywordDict." However, the purpose of this document is to enumerate technical vocabulary to know for the interview as I come across it in LC problem, so I'm still listing these sorts of things as vocabulary to know.

* Hashing
* Heap
* Timsort (python's default sort)
* Self-balancing tree
  * Probably not necessary to know implentation but examples:
  * Red-black
  * AVL
  * Splay
* Maximum subarray
  * Kadane's Algorithm ([P21](/Python3/21.py))
* Recursion
  * Implemented as stack
* Breadth first vs depth first traversal
  * DFS traversal orders
  * Iterative implentations of traversal
* Tail recursion
  * Python does not have tail-call optimization
* Flood fill optimizations such as [span filling](https://en.wikipedia.org/wiki/Flood_fill#Span_filling) ([P733](/Python3/733.py))
* DP
  * Tabulation (bottom up) is better when all subproblems must be calculated ([P53](/Python3/53.py))
* Time complexity of triangular num ([P15](/Python3/15.py))
* collections.defaultdict vs dict.get(key, default)
  * defaultdict creates an entry using the default if not present, faster
  * .get just returns the specified default, less space
* Python Style Guides
  * [PEP8 adapted from Python Docs](https://pep8.org/)
  * [Google](https://google.github.io/styleguide/pyguide.html)
  * [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/style/)
* Python langauge differences
  * Default sort TimSort
  * Modulus floored division
  * No tail-call optimization
