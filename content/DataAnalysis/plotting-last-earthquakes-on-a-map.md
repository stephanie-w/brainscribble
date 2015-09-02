---
title: Plotting Last Earthquakes on a Map
date: 2015-08-30
tags: ipython-notebook
Summary: Plotting the earthquakes of the last 30 months with R and the the National Earthquake Hazards Reduction Program (NEHRP) feed ...

---

Source available on [Nbviewer](http://nbviewer.ipython.org/github/stephanie-w/brainscribble/blob/master/source/plotting-last-earthquakes-on-a-map.ipynb)

The USGS Earthquake Hazards Program is part of the National Earthquake Hazards Reduction Program (NEHRP) and provides several data on earthquake location and magnitude.

The data on earthquakes of the last 30 months is avaiblable at http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv. 

```python
# Render our plots inline
%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
```

### Loading data


```python
dset = pd.read_csv("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv",
                   parse_dates=['time'])
```


```python
dset[:3]
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>depth</th>
      <th>mag</th>
      <th>magType</th>
      <th>nst</th>
      <th>gap</th>
      <th>dmin</th>
      <th>rms</th>
      <th>net</th>
      <th>id</th>
      <th>updated</th>
      <th>place</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-08-30 14:38:41.930000</td>
      <td> 37.1312</td>
      <td> 57.7960</td>
      <td> 12.73</td>
      <td> 4.9</td>
      <td> mb</td>
      <td>NaN</td>
      <td> 61</td>
      <td> 0.836</td>
      <td> 0.82</td>
      <td> us</td>
      <td> us1000365u</td>
      <td> 2015-08-30T16:31:46.684Z</td>
      <td> 26km ENE of Esfarayen, Iran</td>
      <td> earthquake</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-08-30 13:28:01.470000</td>
      <td> 37.7844</td>
      <td> 21.2488</td>
      <td>  8.84</td>
      <td> 4.7</td>
      <td> mb</td>
      <td>NaN</td>
      <td> 44</td>
      <td> 0.809</td>
      <td> 1.35</td>
      <td> us</td>
      <td> us1000365n</td>
      <td> 2015-08-30T14:50:51.030Z</td>
      <td>   5km SW of Savalia, Greece</td>
      <td> earthquake</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-08-30 13:17:34.570000</td>
      <td> 27.6311</td>
      <td> 85.6385</td>
      <td> 10.00</td>
      <td> 4.5</td>
      <td> mb</td>
      <td>NaN</td>
      <td> 83</td>
      <td> 1.089</td>
      <td> 0.67</td>
      <td> us</td>
      <td> us1000365l</td>
      <td> 2015-08-30T16:27:43.556Z</td>
      <td>     11km E of Banepa, Nepal</td>
      <td> earthquake</td>
    </tr>
  </tbody>
</table>
</div>



### Drawing the map


```python
fig = plt.figure(figsize=(14,10))
ax = plt.subplot(1,1,1)
# miller projection
map = Basemap(projection='mill')
x, y = map(dset["longitude"].values, dset["latitude"].values)
magnitude = dset["mag"].values
map.drawcoastlines(color='0.50', linewidth=0.25)
map.fillcontinents(color='0.95')
map.scatter(x,y,s=np.exp(magnitude)*0.3, lw=0.5,
            alpha=0.3, zorder=10, c="m")
plt.show() 
```


![png](figure/plotting-last-earthquakes-on-a-map_5_0.png)



