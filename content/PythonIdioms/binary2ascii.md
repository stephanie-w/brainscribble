---
title: Decoding Binary Code (ascii)
date: 2015-05-08
tags: python
Summary: 

---

```python
def binary2ascii(input):
    result = ""
    x = 0
    while True:
        s = input[x:x+8]
        if not s: break
        sum = 0
        for i in range(len(s)):
            sum += int(s[i]) * 2**(len(s)-i-1)
        result += chr(sum)
        x += 8

    return result
```

Example:


```python
binary2ascii('0110010001100101011000110110111101100100011001010110110101100101')
```




    'decodeme'




