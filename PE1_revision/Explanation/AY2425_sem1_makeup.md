# Q1

## Script design and sub-problem

Start off by identifying the pattern in the sequence, which is

+, -, -, +, -, -,...

Notice that there are 2 - in between the + which hints `n%3==0` as a condition

We are not checking n mod 3 = 1 or 2 explicitly because that can just be shoved under an else statment

Also notice that it is in the form of 2^term (starting from 0)

## Final code
<details>
<summary><b>Solution</b></summary>

```python
def compute_series(n):
    res = 0
    for num in range(n):
        res +=  2**(-num) if num%3==0 else -2**(-num) 
    return round(res, 4)
```

</details>

# Q2
## Script design
Honestly, it is kinda tuff if you don't play around with encode string of different length (odd and even)

Try running encode abc and abcd to see how the function behaves when you have an odd/even length string

```pycon
>>> encode("abc")
'bac'
>>> encode("abcd")
'dbac'
```

Notice that d is concantenated at the front of the string, and bac follows exactly like encode("abc")

It is either 1st or last character added and that depends on the length (is it odd or even) which should hint `if len(s)%2==...`

## Final code
<details>
<summary><b>Solution</b></summary>

```python
def decode(s):
    if len(s) == 1:
        return s
    if len(s) % 2 == 0:
        return decode(s[1:]) + s[0]
    return decode(s[:-1]) + s[-1]
```
</details>