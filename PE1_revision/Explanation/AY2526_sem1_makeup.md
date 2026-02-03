# Q1

## Script design

For a valid bracket pair, there must be an existing open bracket before the close bracket which hints a conditional statement

The checker cannot be a boolean 

Iterate through the string with that condition in mind

## Final code

So the checker is acutally an unpaired open bracket counter

```
def count_matching_bracket(s):
    open_count = 0 
    pairs = 0

    for char in s:
        if char == "(":
            open_count += 1
        if char == ")":
            if open_count > 0:
                open_count -= 1
                pairs += 1
    return pairs
```

# Q2

## Script design

We cannot convert int to str but we can take inspiration

Same old algorithm where we check 1st and 2nd (or last and 2nd last) then slice the string 

Since we are dealing with integers, it is always easier to work from the end 

How to check 2nd last digit? Just remove the 1st digit using floor divide then mod 10 it

Slicing is equivalent to floor dividing 10

## Final code

```
def count_adjacent_pairs(n):
    if n<=9:
        return 0
    if n%10 == (n//10)%10:
            return 1+count_adjacent_pairs(n//10)
    return count_adjacent_pairs(n//10) 
```