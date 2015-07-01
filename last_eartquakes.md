---
title: "Earthquakes Frequency from the past 30 days"
output:
  html_document:
    theme: flatly
    highlight: tango
    
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

```r
library(reshape2)
library(ggplot2)
library(ggmap)
eq <- read.csv("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv", as.is = T)
head(eq[c("time", "longitude", "latitude", "mag")])
```

```
##                       time longitude  latitude  mag
## 1 2015-07-01T08:21:55.900Z -121.7202  36.96550 1.73
## 2 2015-07-01T08:01:31.650Z -115.6068  33.17283 2.73
## 3 2015-07-01T07:48:30.000Z -150.8982  63.09950 3.10
## 4 2015-07-01T07:32:53.000Z -149.2750  64.73590 2.30
## 5 2015-07-01T07:02:45.000Z -151.0643  60.17560 2.00
## 6 2015-07-01T06:54:59.070Z  169.2641 -13.02010 4.50
```

```r
eq$area <- factor(sub("^[^,]+, ", "", eq$place))

eq$date <- as.Date(strtrim(eq$time, 19), format = "%Y-%m-%dT%H:%M:%S")
eqFreq1 <- table(eq$date, eq$mag, eq$area)
eqFreq2 <- melt(eqFreq1)
names(eqFreq2) <- c("date", "M", "area", "freq")
head(subset(eqFreq2, freq > 0 & M > 0))
```

```
##             date   M        area freq
## 10771 2015-06-14 4.1 Afghanistan    3
## 10778 2015-06-21 4.1 Afghanistan    1
## 10784 2015-06-27 4.1 Afghanistan    1
## 10810 2015-06-22 4.2 Afghanistan    1
## 10827 2015-06-08 4.3 Afghanistan    1
## 10834 2015-06-15 4.3 Afghanistan    2
```

```r
eqFreq2$M <- factor(round(eqFreq2$M))
ggplot(eqFreq2, aes(date, weight = freq, fill = M)) + geom_bar(binwidth = 60 * 60 * 24) + labs(x = "Date", y = "Frequency", title = "Earthquakes Frequency from the past 30 days") + theme(axis.text.x = element_text(angle = 90, 
    hjust = 1))
```

<div class="rimage center"><img src="fig/unnamed-chunk-1-1.png" title="plot of chunk unnamed-chunk-1" alt="plot of chunk unnamed-chunk-1" class="plot" /></div>

```r
world_map <- map_data("world")
p <- ggplot() + coord_fixed() + xlab("") + ylab("")
base_world <- p + geom_polygon(data = world_map, aes(x = long, y = lat, group = group), colour = "light green", fill = "light green")

base_world + geom_point(aes(x = longitude, y = latitude, size = mag), data = eq, colour = "Deep Pink", fill = "Pink", pch = 21, alpha = I(0.7))
```

<div class="rimage center"><img src="fig/unnamed-chunk-1-2.png" title="plot of chunk unnamed-chunk-1" alt="plot of chunk unnamed-chunk-1" class="plot" /></div>

