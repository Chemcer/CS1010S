# Compilation Q4 AY2110 Q1

## Script design
The main challenge for this question is identifying the pattern

Notice that 2n-1 honeycombs are added to the f(n-1), we can try to identify a recurrence relation for this by referring to the image

The honeycomb is built by adding 2n-1 hexagons on top of the previous layer, we need to consider the number of overlapping walls

In the outermost layer, notice that there is definitely an overlap with the previous honeycomb structure and that when written out, it is 3, 7, 11,... an arithematic progression 3+4(n-2) (-2 because we are starting from n = 2)

Within the outermost layer, we see that there is an overlap at the side that is in the form of 2(n-1)

We can then create a recurrence relations, outermost hive contains 6(number of walls in a hexagon) * (2n-1) (number of hexagons added) - (3 + 4(n-2)) (overlapping walls with the u_(n-1)) - 2*(n-1) (overlapping walls in the outermost layer)

This yields the recurrence relation $u_n = u_{n-1} + 6n + 1, n \geq 2$ (the same as the solution provided)

## Final code

<details>
<summary><b>Solution</b></summary>

```python
def num_walls(n):
    if n == 0:
        return 0
    if n == 1:
        return 6
    return num_walls(n-1) + 6n + 1
```
</details>

# Compilation Q5A AY1720 Q1

## Script design

Pretty obvious that we are making more and more triangles

Notice that in each black triangle, the next sequence makes 4 triangles 1/4 the size of a particular triangle, 1 white 3 black

Also notice that the next sequence adds a value (number of new, smaller triangles made) to the previous sequence

Pretty similar to Q4, we have to make a recurrence relation based on how new triangles are made. This is simpler than Q4 as there is no overlaps involved

Knowing that the sequence adds a value to the previous term, it can be rewritten as 1, 1+4, 5+12, 17+36

This yields $u_n = u_{n-1} + 4 \cdot 3^{n-1}$ then we convert this to code

## Final code

<details>
<summary><b>Solution</b></summary>

```python
def num_triangles(n):
    if n==0:
        return 1
    return num_triangles(n-1) + 4*3**(n-1)
```
</details>

# Compilation 5B AY1720 Q1

## Script design

We have identified the number of new white and black triangles made, 1 new white triangle in each black traingle and it is 1/4 the size of black triangle

As such, we are removing a quarter of the total area from the previous term, which is equivalent to returning 3/4 of the previous area

## Final code

<details>
<summary><b>Solution</b></summary>

```python
def area(n):
    if n==0:
        return 1
    return 3 * area(n-1) / 4
```

</details>

# Compilation Q6A AY1710 Q1

## Script design

The idea is pretty straightforward, check if the current character is a alphabet or number. By default, we always take it as 1 atom unless it is followed by a number, then we have to increase the number of atoms to that value

Since the default is 1, we have to create a `(temp - 1) + int(index)`. -1 to remove the existing 1 atom and +int(index) to get the value of the atoms

I think the iterative is pretty straightforward once we realise that we have to create a res and temp then reset temp

What if we want to do it recursively? The same logic (temp - 1) applies

## Final code

<details>
<summary><b>Solution iterative</b></summary>

```python
def num_atoms(molecules):
    res = 0
    for char in molecules:
        if char.isalpha: 
            res += 1
        else:
            res = res -  1 + int(char)
    return res
```
</details>

<details>
<summary><b>Solution recursive</b></summary>

```python
def num_atoms(molecules):
    if len(molecules)==0:
        return 0
    if molecules[0].isalpha():
        return 1 + num_atoms(moelcules[1:])
    return num_atoms(molecules[1:]) - 1 + int(molecules[0])
```

</details>

# Compilation Q6B AY1710 Q1

## Script design 

I am not going to bother with recursion 

We have to store the atomic mass of each element in each itereative round and multiply it by a number if the next char is a digit

By storing atomic masss, we have to consider the fact that we have to reset the variable in each iterative loop, to do that, we end the loop with conndition and temp = 0 (anything that resets temp will work)

The 2 conditions are is it a digit or is it a alphabet

If it is a alphabet, store the atomic mass in temp variable and add it to the result. We have to add it because the lasst char of the string might be an alphabet

If it is a digit, multiply it to the temp value and result - atomic mass + new

## Final code

<details>
<summary><b>Solution</b></summary>

```python
def molar_mass(molecule):
    temp = 0
    res = 0
    for char in molecule:
        if char.isalpha():
            temp =  atomic_mass(char)
            res += temp
        else:
            res += (int(char) - 1)*temp
            temp = 0
    return res
```

</details>

# Compilation Q7A AY2310 Q2

## Script design 

Main issue:

Notice that we alternate the use of helper function and without the use of helper. Can use a flag to switch between helper and no helper

Alternatively, convert int to str

## Final code

<details>
<summary><b>Solution integers</b></summary>

```python
def get_sum(num):
    res = 0
    flag = True
    while num!=0:
        res += helper(num%10) if flag else num%10
        flag = not flag
        num = num//10
    return res
```

</details>

<details>
<summary><b>Solution strings</b></summary>

```python
def get_sum(num):
    num = str(num)
    num = num[::-1]
    for idx in range(len(num)):
        res += helper(int(num)%10) if idx%2==0 else int(num)%10
    return res
```

</details>

# Compilation Q7B AY2310 Q2

## Script design

If working in terms of integers, it is pretty annoying to alternate between return with helper and return without helper. As such, we just lump helper and no helper together, so take n%10 and (n%100)//10 to separate the ones and tens place

I will think about the strings approach on another day

## Final code
<details>
<summary><b>Solution integers</b></summary>

```python
def get_num(num):
    if num==0:
        return 0
    return helper(n%10) + (n%100)//10 + get_num(n//100)
```

</details>
 
# Compilation Q7C AY2310

## Script design

Input is a 15 digit integer and we need to find the last integer to make a valid number (n mod 10 == 0), as such we can find the sum of the 15 digit num using the already written out luhn algorithm

As the condition is n mod 10 == 0, the entire thing can be simplified by only considering the ones place of the check sum 

## Final code

<details>
<summary><b>Solution</b></summary>

```python
def make_valid(num):
    return (10 - get_num(num)%10)%10
```

</details>

# Compilation Q8A AY1810 Q2

## Scipt design

Compare the nth and n+1th character, if it is the same, we add 1 and cut out s[0] to reduce problem size. Quite similar to other string recursion algortihms, this is probably easier

Since we are comparing character and next character, we have to stop at len(s)==1 or else it returns an out of index error

## Final code

<details>
<summary><b>Solution</b></summary>

```python
def num_pairs(s):
    if len(s)<=1:
        return 0
    if s[0] == s[1]:
        return 1 + num_pairs(s[1:])
    return num_pairs(s[1:])
```

</details>

# Compilation Q8B AY1810 Q2

## Script design

Same idea as above honestly

## Final code

<details>
<summary><b>Solution while loop</b></summary>

```python
def num_pairs(s):
    res = 0
    pos = 0
    while pos<len(s)-2:
        if s[pos] == s[pos+1]:
            res +=1
        pos +=1
    return res
```

</details>

<details>
<summary><b>Solution for loop</b></summary>

```python
def num_pairs(s):
    res = 0
    for idx in range(len(s) - 1):
        if s[idx]==s[idx+1]:
            res += 1
    return res
```

</details>

# Compilation Q8C AY1810 Q2

## Script design

Checking for repeated characters in the string, which is the same as s[start:end]==n*s[start]. Notice that if the length of s is less than n, it will never be true so we can stop at len(s) < n

Once the logical condition has been identitfied, the rest of the algo should be pretty manageable

## Final code

<details>
<summary><b>Solution recursive</b></summary>

```python
def num_consec(s, n):
    if len(s) < n:
        return 0
    if s[:n] == n*s[n]:
        return 1 + num_consec(s[1:])
    return num_consec(s[1:])
```

</details>

<details>
<summary><b>Solution iterative</b></summary>

```python
def num_consec(s, n):
    res = 0:
    for idx in range(len(s)-n):
        if s[idx:idx+n] == n*s[idx]:
            res += 1
    return res
```

</details>