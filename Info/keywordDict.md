# DSA Dictionary

Note I am only adding to this document AS I COME ACROSS things that I don't know.

## Data Types

### List

**Initialize:**

```python
myList = [1, 2, 3]
myList = ['a', 'b', 'c']
myList = [0]*26
myDigitsList = [i for i in range(10)]
```

Note that the last list is initialized with 26 0's

**Append:**

```python
temp = [1,2]
temp.append(3)
temp == [1,2,3]
```

### String

Note that strings are arrays. However, there is no character data type, just strings of length 1.

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

**To Lowercase:** `myStr.lower()` (Note this returns a string, not in place)

**Check if alphanumeric:** `myStr.isalnum()`

### Set

**Initialize:**

```python
mySet = {"apple", "banana", "cherry"}
emptySet = set()
```

Check if contains: `if "apple" in mySet`

**Append:**

```python
mySet = {1, 2}
mySet.add(3)
mySet == {1, 2, 3}
```

(Note that set is technically unordered)

### Dictionary

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

### Stack/Queue

Stacks and queues are typically implemented using python's deque (pronounced "deque") module, short for double-ended queue. This means that you can pop or push from either the left or right end

**Initialize:**

```python
from collections import deque

myDeque = deque()
myDeque = deque([1,2,3])
```

Note in the following sections that the push vs pop for stack vs queue is technically arbitrary.

For stack, pop from the same side you push, and for queue, pop from the opposite side you push. I just have the following preferences:

#### As a Stack

**Push:** `myStack.append(1)`

**Pop:** `myStack.pop()` (Note this returns the popped value as well)

**Access:** `frontVal = myStack[-1]`

#### As a Queue

**Push:** `myQ.append(1)`

**Pop:** `myQ.pop()`

**Access:** `myQ[0]`

## Algorithms

### Max

```python
myList = [1,2,3]
max(myList)==3
max(1,2,3)==3
```

### Floor

```python
from math import floor
floor(1.2)==2
```

Note that floor is commonly used with division, such as in finding a midpoint for binary search ([P704](/Python3/704.py))

In this case, you can use the integer division operator: `3//2==1`

### Sort

Note that python uses [Timsort](https://en.wikipedia.org/wiki/Timsort#), which is stable and O(nlogn)

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

### Unpacking

Use the `*` to unpack an iterable in python.

My main use for this has been copying values of lists:

```python
myDeepCopy = [*myList]
myStrList = [*myString]
```

### Change data type

str to list: `myList = list(myStr)` or `myList = [*myStr]`

char to int: `myInt = ord(myChar)`

list to str: `myStr = str(myList)` (Note that the result looks like `"[1, 2, 3]"` as if in console)

list of strings to string: `myStr = ''.join(myStrList)`

list to tuple: `myTuple = tuple(myList)`

list to set (removes duplicates): mySet = `set(myList)`

### Length

```python
len(object)
```

returns number of items in an object or characters in string

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
* Tail recursion
  * Python does not have tail-call optimization
* Flood fill optimizations such as [span filling](https://en.wikipedia.org/wiki/Flood_fill#Span_filling) ([P733](/Python3/733.py))
* DP
  * Tabulation is better when all subproblems must be calculated ([P53](/Python3/53.py))

I hope I add more to this since it's funny when the description is so long compared to the actual list.
