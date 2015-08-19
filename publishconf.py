#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://stephanie-w.github.io/blog'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

#template settings
SHOW_ARTICLE_AUTHOR = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

PROFILE_IMAGE_URL = "http://stephanie-w.github.io/blog/images/post_1246903_635089122565391744.jpg"
BOOTSTRAP_THEME = "lumen"
#SITELOGO = "images/post_1246903_635089122565391744.jpg"
SIDEBAR_IMAGES = ["http://stephanie-w.github.io/blog/images/post_1246903_635089122565391744.jpg"]
FAVICON = "images/post_1246903_635089122565391744.jpg"
BOOTSTRAP_NAVBAR_INVERSE = False

PYGMENTS_STYLE = 'solarized'
