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

### Range

Note that I pretty much only use `range()` in for loops, so this description will reflect that. Note that range actually returns a range object, but is as an iterable for my purposes

**Initialize:**

```python
range(start=0, stop, step=1)
```

Note that `start=0` and `step=1` indicates that these are optional parameters, and gives their default value.

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

#### As a Stack

**Push:** `myStack.append(1)`

**Pop:** `myStack.pop()` (Note this returns the popped value as well)

**Access:** `frontVal = myStack[-1]`

## Algorithms

### Sort

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

### Change data type

str to list: `myList = list(myStr)`

char to int: `myInt = ord(myChar)`

list to str: `myStr = str(myList)` (Note that the result looks like `"[1, 2, 3]"` as if in console)

list of strings to string: `myStr = ''.join(myStrList)`

list to tuple `myTuple = tuple(myList)`

### Length

```python
len(object)
```

returns number of items in an object or characters in string

### Enumerate (For loop with index and item)

Takes a collection and gives an id to each item, useful to get features of a traditional and enhanced for loop

```python
for index, value in enumerate(nums):
  print("The index is", index)
  print("The value is", value)
```

## Other concepts to understand

I think the best way to explain this section is to just explain why I decided to add it. In P347, I used the heapq module, and I think in an interview it's reasonable to expect an interviewer to check if I understand heaps in general. Since that knowledge isn't required to write the python code, I won't go into full detail since this is a "keywordDict." However, the purpose of this document is to enumerate technical vocabulary to know for the interview as I come across it in LC problem, so I'm still listing these sorts of things as vocabulary to know.

* Heap
* Self-balancing tree
  * Probably not necessary to know implentation but examples:
  * Red-black
  * AVL
  * Splay

I hope I add more to this since it's funny when the description is so long compared to the actual list.
