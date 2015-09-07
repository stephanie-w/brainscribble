---
title: Casear Cypher Encoding
date: 2015-05-08
status: draft
tags: python
Summary: 

---

```python
import string

ascii = ''.join([chr(x) for x in range(256)])
def decypher(s, n):
    trans = string.maketrans(ascii, ascii[n:] + ascii[:n])
    return s.translate(trans)


if __name__ == '__main__':
    s = raw_input('Enter a string to decipher ').upper()
    n = raw_input('Enter a number ')
    if not n:
        for i in range(256):
            print decypher(s, i)
    else:
        n = int(n)
        print decypher(s, n)
```
