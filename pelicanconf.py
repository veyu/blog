#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'veyu'
PROFILE_IMAGE = 'avatar_200.png'
SITENAME = "dev remorses"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/veyu'),
          ('linkedin', 'https://linkedin.com'),)

DEFAULT_PAGINATION = 10

THEME = '../veyu-pelican-hydra'

ARTICLE_URL = "{category}/{date:%Y}/{date:%b}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{date:%Y}/{date:%b}/{date:%d}/{slug}.html"
PAGE_URL = "pages/{slug}.html"
PAGE_SAVE_AS = "pages/{slug}.html"

DEFAULT_DATE_FORMAT = '%d %B %Y'

STATIC_PATHS = [ "images",
                 "extra/favicon.ico"]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': { 'path': 'favicon.ico' }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
