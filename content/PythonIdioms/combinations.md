---
title: All possible combinations
date: 2015-05-08
tags: python
Summary: 

---

Use :

    itertools.combinations(iterable, r)

or the following code:


```python
from itertools import product, compress
items = ['A', 'B', 'C', 'C', 'D']

list( set(compress(items,mask)) 
     for mask in product(*[[0,1]]*len(items)) )
# alternative: ...in product([0,1], repeat=len(items)) )
```




    [set(),
     {'D'},
     {'C'},
     {'C', 'D'},
     {'C'},
     {'C', 'D'},
     {'C'},
     {'C', 'D'},
     {'B'},
     {'B', 'D'},
     {'B', 'C'},
     {'B', 'C', 'D'},
     {'B', 'C'},
     {'B', 'C', 'D'},
     {'B', 'C'},
     {'B', 'C', 'D'},
     {'A'},
     {'A', 'D'},
     {'A', 'C'},
     {'A', 'C', 'D'},
     {'A', 'C'},
     {'A', 'C', 'D'},
     {'A', 'C'},
     {'A', 'C', 'D'},
     {'A', 'B'},
     {'A', 'B', 'D'},
     {'A', 'B', 'C'},
     {'A', 'B', 'C', 'D'},
     {'A', 'B', 'C'},
     {'A', 'B', 'C', 'D'},
     {'A', 'B', 'C'},
     {'A', 'B', 'C', 'D'}]



that uses this generated mask:


```python
list(product(*[[0,1]]*len(items)))
```




    [(0, 0, 0, 0, 0),
     (0, 0, 0, 0, 1),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 1, 1),
     (0, 0, 1, 0, 0),
     (0, 0, 1, 0, 1),
     (0, 0, 1, 1, 0),
     (0, 0, 1, 1, 1),
     (0, 1, 0, 0, 0),
     (0, 1, 0, 0, 1),
     (0, 1, 0, 1, 0),
     (0, 1, 0, 1, 1),
     (0, 1, 1, 0, 0),
     (0, 1, 1, 0, 1),
     (0, 1, 1, 1, 0),
     (0, 1, 1, 1, 1),
     (1, 0, 0, 0, 0),
     (1, 0, 0, 0, 1),
     (1, 0, 0, 1, 0),
     (1, 0, 0, 1, 1),
     (1, 0, 1, 0, 0),
     (1, 0, 1, 0, 1),
     (1, 0, 1, 1, 0),
     (1, 0, 1, 1, 1),
     (1, 1, 0, 0, 0),
     (1, 1, 0, 0, 1),
     (1, 1, 0, 1, 0),
     (1, 1, 0, 1, 1),
     (1, 1, 1, 0, 0),
     (1, 1, 1, 0, 1),
     (1, 1, 1, 1, 0),
     (1, 1, 1, 1, 1)]



see
[Python code to pick out all possible combinations from a list?](http://stackoverflow.com/questions/464864/python-code-to-pick-out-all-possible-combinations-from-a-list)
