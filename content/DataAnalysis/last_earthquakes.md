---
title: R: Earthquakes from the past 30 days
tags: R
date: 2015-06-23
Image: figure/earthquakes_worldmap-1.png
summary: Plotting the earthquakes of the last 30 months with R and the earthquake.usgs.gov feed.

---

Earthquakes of the last 30 months from the earthquake.usgs.gov feed : http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php feed. 


Below are the fields included in the spreadsheet output:

    time
    latitude
    longitude
    depth
    mag
    magType
    nst
    gap
    dmin
    rms
    net
    id
    updated
    place

Loading libraries and downloading the feed:

```r
library(reshape2)
library(ggplot2)
library(ggmap)
eq <- read.csv("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv", as.is = T)
head(eq[c("time", "longitude", "latitude", "place", "mag")])
```

```
##                       time longitude latitude
## 1 2015-08-20T22:41:58.790Z -117.1827 34.00583
## 2 2015-08-20T22:09:37.180Z -121.5903 36.76000
## 3 2015-08-20T21:38:51.403Z -119.6169 41.87000
## 4 2015-08-20T21:27:08.570Z  -98.1158 36.69730
## 5 2015-08-20T21:24:43.900Z  -64.5836 19.71500
## 6 2015-08-20T21:17:33.170Z -116.4987 33.49567
##                                          place  mag
## 1                6km S of Redlands, California 0.92
## 2             7km ESE of Prunedale, California 1.43
## 3                 69km ESE of Lakeview, Oregon 2.48
## 4                  21km NE of Helena, Oklahoma 2.70
## 5 143km N of Road Town, British Virgin Islands 3.40
## 6                 18km ESE of Anza, California 0.58
```

Preprocessing the data:

```r
eq$area <- factor(sub("^[^,]+, ", "", eq$place))
eq$date <- as.Date(strtrim(eq$time, 19), format = "%Y-%m-%dT%H:%M:%S")
```

Building a new dataset with magnitude frequencies by day:

```r
eqFreq1 <- with(eq, table(date, mag))
eqFreq2 <- melt(eqFreq1)
names(eqFreq2) <- c("date", "magnitude", "freq")
head(subset(eqFreq2, freq > 0 & magnitude > 0))
```

```
##            date magnitude freq
## 1149 2015-07-22      0.01    1
## 1150 2015-07-23      0.01    1
## 1155 2015-07-28      0.01    1
## 1156 2015-07-29      0.01    1
## 1168 2015-08-10      0.01    1
## 1173 2015-08-15      0.01    1
```

Plotting a stacked bars graph of earthquakes magnitude frequencies by day:

```r
eqFreq2$magnitude <- factor(round(eqFreq2$magnitude))
ggplot(eqFreq2, aes(date, weight = freq, fill = magnitude)) +
        geom_bar(binwidth = 60 * 60 * 24) +
        labs(x = "Date", y = "Frequency", 
             title = "Earthquakes Frequency from the past 30 days") +
        theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
        scale_fill_brewer(palette="BuPu")
```

<div class="rimage center"><img src="figure/earthquakes_frequency-1.png" title="plot of chunk earthquakes_frequency" alt="plot of chunk earthquakes_frequency" class="plot" /></div>

Using the original dataset to plot a map with the locations of the 100 biggest earthquakes:

```r
BiggestMag <- tail(sort(eq$mag), n=100)
#Plotting
world_map <- map_data("world")
ggplot() + coord_fixed() + xlab("") + ylab("") +
        geom_polygon(data = world_map, 
                     aes(x = long, y = lat, group = group), 
                     colour = "light green", fill = "light green") +
        geom_point(aes(x = longitude, y = latitude, size = mag),
                   data = eq[eq$mag %in% BiggestMag ,], 
                   colour = "Deep Pink", fill = "Pink", 
                   pch = 21, alpha = I(0.7)) +
        labs(title="Biggest earthquakes from the past 30 days")
```

<div class="rimage center"><img src="figure/earthquakes_worldmap-1.png" title="plot of chunk earthquakes_worldmap" alt="plot of chunk earthquakes_worldmap" class="plot" /></div>
