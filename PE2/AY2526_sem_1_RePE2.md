# Q1 Print Hollow Pyramid

## Question

Implement a function hollow_pyramid that takes in a positive integer, n, where n > 0, and prints the following pattern:

- a hollow pyramid of height n centered with borders and central vertical line

- left and right borders are '\*', and

- central vertical (middle column) is '\*' and bottom row is filled with '\*'

## Algo breakdown

Notice that top and bottom rows are different from the rows in-between, so the easy way to go about it is to manually print those out

### Making rows with 3 '*'

Notice that it folllows a asterisk space astrisk space astrisk pattern, number of space is row-1 where row starts from 1

So each row will be in the form 

```python
for row in range(1,n-1):
    line = '*' + ' '*(row - 1) + '*' + ' '*(row - 1) + '*' 
```

### Centering

By observation, the length of base is given as n + n - 1 = 2n - 1, either center string methods (easier) or calculate the number of spaces needed

```python
print(line.center(2 * n - 1))
```

### Creating the pyramid 

### The top row

Of course it is simply `print(linne.center(2*n - 1))`

Notice that n == 1 is a possiblity, you can choose the `return None` to stop the function or place the last row in the for loop

### The bottom row

From our initial implementation, I have avoided the last row, so we can just change it to `for row in range(1, n)`

Then we need a condition `if row != n` to ensure that we print the 3 '\*' and an `else` to print the last row which is `'*' * (2 * n -1)`

## Solution

```python
def hollow_pyramid(n):
    start = '*'
    print(start.center(2 * n -1))
    for row in range(1, n):
        if row != n:
            line = '*' + ' '*(row - 1) + '*' + ' '*(row - 1) + '*' 
            print(line.center(2 * n -1))
        else:
            print('*' * (2 * n -1))
```

# Q2 Convert Values to Keys

## Question

You are given a dictionary that maps keys to values. Each value in a dictionary may be one of the following types: `int`, `float`, `str`, `list`, or `tuple` but not a dict. The lists or tuples may also be nested.

Your task is to implement a function value_to_key(d) that produces a new dictionary, mapping each unique atomic value to a list of keys from the original dictionary in which that atomic value appears. An atomic value is any value that is not a list or a tuple. That is, it is either an `int`, a `float`, or a `str`. Strings are treated as atomic values (do not iterate over characters).

## Qn breakdown

Qn just wants key value representation to value key format

As such there will be a `res[value] = key` line. Since the value might be a list/tuple we can just iterate through it 

### Problem tuple/list value that may be nested

If list/tuple is not nested, then there is not much issues since we can safely iterate through the items in list/tuple

When the tuple/list is nested, we cannot simply iterate through the list/tuple because we will then hit another tuple/list

#### Flatten list/tuple

Function will iterate through until it reaches another tuple/list, then just (recursively) call the function again to ensure 'remove' the inner tuple/list 

Recursive function call is needed as there can exist a data such as [1, [2, [3, [4,]]]]. A simple extend list method will not account for inner inner lists/tuples

```python
def flatten(data):
    if type(data) not in (list, tuple):
        return data
    res = []
    for item in data:
        if type(item) in (list, tuple):
            res.extend(flatten(item))
        else:
            res.apped(item)
    return res
```

### Conversion

Since we have dealt with the case where there are multiple nested list/tuple, we can now get all key value pairs and create new dictionary

Due to the implementation of flatten, got to check the type that the function returns, if not it will raise a type error or go against qn requirement (not to iterate through string)

```python
res = {}
for key, value in d.items():
    flatten_value = flatten(value)
    if type(flatten_value) not in (list, tuple):
        if flatten_value not in res:
            res[flatten_value] = []
        if key not in res[flatten_value]:
            res[flatten_value].append(key)
    else:
        for item in flatten_value:
            if item not in res:
                res[item] = []
            if key not in res[item]
                res[item].append(key)
    return res
```

## Solution

To make it neater, flatten will return a list no matter the input (string, int, float will be in a list now)

```python
def flatten(item):
    if type(item) not in (list, tuple):
        return [item]
    res = []
    for val in item:
        if type(val) in (list, tuple):
            res.extend(flatten(val))
        else:
            res.append(val)
    return res

def value_to_key(d):
    res = {}
    for key, value in d.items():
        flatten_value = flatten(value)
        for item in flatten_value:
            if item not in res:
                res[item] = []
            if key not in res[item]:
                res[item].append(key)
    return res
```