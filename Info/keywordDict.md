# DSA Dictionary

Note I am only adding to this document AS I COME ACROSS things that I don't know.

## Data Types

### List

**Initialize:**

```python
myList = [1, 2, 3]
myList = ['a', 'b', 'c']
myList = [0]*26
```

Note that the last list is initialized with 26 0's

### Set

**Initialize:**

```python
mySet = {"apple", "banana", "cherry"}
emptySet = set()
```

Check if contains: `if "apple" in mySet`

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

## Concatenate

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

### Append

**Lists:**

```python
temp = [1,2]
temp.append(3)
temp == [1,2,3]
```

**Dictionary:**

```python
myDict = {1: "One"}
myDict[2] = "Two"
myDict == {
  1: "One",
  2: "Two"
}
```

**Set:**

```python
mySet = {1, 2}
mySet.add(3)
mySet == {1, 2, 3}
```

(Note that set is technically unordered)

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
