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

All objects in elems1 are the same means we check all elements in elems1