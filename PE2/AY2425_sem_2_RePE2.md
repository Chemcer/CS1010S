# Q1, Soda Can

## Question

Ados really likes to drink soda from a can. One day, he found that a can of soda can be recycled for money. Every time Ados recycles k cans of soda, he receives enough money to buy another can of soda. This means more soda for him to drink.

Implement the function soda(n, k) , which takes two integers, n and k . n corresponds to the initial number of soda cans and k corresponds to the number of empty cans that needs to be recycled to buy another can of soda. The function returns the total number of soda that Ados can drink if he recycles.

## breakdown

Convert all n cans to empty cans then we find how many new soda cans can be bought, then repeat over and over again. n mod k + n//k --> if >= k then we buy again, repeating this cycle until n//k == 0

## Solution

```python
def soda(n, k):
    res = n
    while n//k:
        temp, empty = divmod(n, k)
        res += temp
        n = temp + empty
    return res
```

# Q2, All in Any

Implement the function all_in_any(elems1, elems2) , which takes two tuples, elems1 and elems2 . The function returns:

1. True if elems1 is empty. In this case, we ignore the contents of elems2.

2. True if all of the following conditions are satisfied.

- elems1 is not empty

- All objects in elems1 are the same

- All objects is the same as at least one value in elems2

3. False otherwise.

Two objects X and Y are considered to be the same if X and Y have the same type and values.

## Breakdown

Deal with the easiest case first, instantly return true is elems1 is empty

Case 2 is annoying since there 2 conditions to meet

All objects in elems1 are the same means we check all elements in elems1. Recall that if A = B, B = C,... then A = B = C =... Hence we check if every other elements in elems1 is the same as the 1st element in elems1. If one of it is not equal, then we can simply return False

2nd condition is 'All objects is the same as at least one value in elems2', so we can simply iterate through elems2 to see if it appears once and has the same data type. Because of the data type, we cannot use elems1[0] in elems2 to check

To check if all elements in elems1 are the same,

```python
for item in elems1:
    if type(item) != type(elems1[0]) or item != elems[0]:
        return False
    else:
        pass # passing the first criteria  
```

To check if elems1 exists in elems2

```python
for item in elems2:
    if item == elems1[0] and type(item) == type(elems1[0]):
        return True
```

## Solution

Combine all those in sequence then end it with a return False (failing the conditions in case 2)

Alternatively, use in built all and any function lol

```python
def all_in_any(elems1, elems2):
    if not elems1:
        return True
    if all(type(elems1[0]) == type(x) and elems1[0]==x for x in elems1):
        return any(type(elems1[0]) == type(x) and elems1[0]==x for x in elems2)
    return False
```
