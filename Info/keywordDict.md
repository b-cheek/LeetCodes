# DSA Dictionary

Note I am only adding to this document AS I COME ACROSS things that I don't know.

## Data Types

### List

Initialize:

```python
myList = [1, 2, 3]
myList = ['a', 'b', 'c']
myList = [0]*26
```

Note that the last list is initialized with 26 0's

### Set

Initialize:

```python
mySet = {"apple", "banana", "cherry"}
emptySet = set()
```

Check if contains: `if "apple" in mySet`

### Dictionary

Initialize:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
emptyDict = {}
```

Access: `thisdict["brand"] == "Ford"`

OR

```python
thisdict.get("brand", None) == "Ford"
```

but will return `None` if there is no brand key.

Iterate:

```python
for key in myDict:
    print(myDict[key])
```

## Algorithms

### Sort

Any iterable:

```python
sorted(iterable, key=key, reverse=reverse)
```

Returns sorted iterable

[W3 page](https://www.w3schools.com/python/ref_func_sorted.asp)

Lists:

```python
list.sort(reverse=True|False, key=myFunc)
```

Modifies list in place

[W3 page](https://www.w3schools.com/python/ref_list_sort.asp)

## Concatenate

Strings:

```python
part1 = 'py'
part2 = 'thon'
myStr = part1 + part2
print(myStr)
```

`python`

Works generally how you think, with += as well, etc.

Items of an iterable:

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

### Length

```python
len(object)
```

returns number of items in an object or characters in string
