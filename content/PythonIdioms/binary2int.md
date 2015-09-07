---
title: Decoding Binary Code (int)
date: 2015-05-08
tags: python
Summary: 

---

```python
int('11111111', 2)
```




    255




```python
def binary2int(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i]) * 2**(len(s)-i-1)
    print sum
```


```python
binary2int('11111111')
```

    255



