---
title: A docker container for the "Data Science at the Command Line" book 
date: 2016-02-19
Pin: true

---

[docker-data-science-at-the-command-line](https://github.com/stephanie-w/docker-data-science-at-the-command-line) contains everything to build a doker container to use with the book [Data Science at the Command Line](http://datascienceatthecommandline.com).


To build the container :

    cd docker--t data-science-toolbox .
    docker build -t data-science-toolbox .

To run the container :

    docker run -v `pwd`:/data -it --rm data-science-toolbox /bin/bash

