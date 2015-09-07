---
title: Encoding/Decoding Vigenere Cypher
date: 2015-05-08
tags: python
Summary: 

---

```python
import string
def vigenere(c,k,e=1):
    # e=1 to encrypt, e=-1 to decrypt
    wk=[string.ascii_uppercase.find(ch) for ch in k.upper()]
    wc=[string.ascii_uppercase.find(ch) for ch in c.upper()]
    wc = [ (x[0]+(e*x[1]))%26 for x in zip(wc,wk*(len(wc)/len(wk)+1))]

    return string.join([string.ascii_uppercase[x] for x in wc],"")
```

Example:


```python
vigenere('Encodeme', 'mypassphrase', 1)
```




    'QLROVWBL'




```python
vigenere('QLROVWBL', 'mypassphrase', -1)
```




    'ENCODEME'




