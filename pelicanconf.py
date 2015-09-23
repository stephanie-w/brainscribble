#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Stephanie W'
SITENAME = u'Brain Scribble'
SITEURL = ''

PATH ='content/'
OUTPUT_PATH = 'output/'
SLUGIFY_SOURCE = 'basename'
USE_FOLDER_AS_CATEGORY = True

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

#template settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU =  True

LINKEDIN_ADDRESS = "https://fr.linkedin.com/pub/stephanie-werli/26/b69/a0b"
GITHUB_ADDRESS = "https://github.com/stephanie-w"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE = 'fs'
IGNORE_FILES = ['*.Rmd', '*.ipynb']

#Plugins
PLUGIN_PATHS = ['/home/stephanie/git/pelican/pelican-plugins/']
PLUGINS = ['code_include','extract_toc','related_posts','better_codeblock_line_numbering']

PLUGINS += ['render_math']
MATH_JAX = {
   'process_summary': True,
   'auto_insert': False,
}

PLUGINS += ['summary']
SUMMARY_BEGIN_MARKER = '<!-- BEGIN_SUMMARY -->'
SUMMARY_END_MARKER = '<!-- END_SUMMARY -->'

PLUGINS += ['series']
DISPLAY_SERIES_ON_SIDEBAR = True
SHOW_SERIES = True

PLUGINS += ['representative_image']

PLUGINS += ['clean_summary']
CLEAN_SUMMARY_MAXIMUM = 0
CLEAN_SUMMARY_MINIMUM_ONE = False

PLUGINS += ['pin_to_top']

PLUGINS += ['feed_summary']
FEED_USE_SUMMARY = True

PLUGINS += ['tag_cloud']


from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension
MD_EXTENSIONS = [
    CodeHiliteExtension(css_class='highlight'),
    TocExtension(permalink=True),
    CodeHiliteExtension(css_class='highlight', linenums=False),
    TocExtension(),
    'markdown.extensions.extra',
]
 

# Blogroll
LINKS = (('codeeval Profile', 'https://www.codeeval.com/profile/lisptick/'),
('hackerrank Profile', 'https://www.hackerrank.com/lisptick'),
('Tableau Profile', 'https://public.tableau.com/profile/stephanie.w3667#!/'))
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)


# Social widget
SOCIAL = (('linkedin', 'https://fr.linkedin.com/pub/stephanie-werli/26/b69/a0b'),
          ('github', 'http://github.com/stephanie-w'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# global metadata to all the contents
DEFAULT_METADATA = {}

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'figure',
    'images',
    'extra/robots.txt',
    ]

BOOTSTRAP_FLUID = True
DISPLAY_TAGS_ON_SIDEBAR = True
