#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.insert(0, '.')
from local import settings
sys.path.insert(0, settings.plugins_repo_path)

AUTHOR = u'NoCoolName Tom'
AUTHOR_EMAIL = u'nocoolnametom@gmail.com'
SITENAME = u'NoCoolName Blog'
SITEURL = settings.regular_siteurl

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

HTML_LANG = 'en'

THEME = "built-texts"

FILES_TO_COPY = (('extra/.htaccess', '.htaccess'), ('extra/robots.txt', 'robots.txt'),)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('My Technical Blog', 'http://blog.tomdoggett.net/'),
          ('My Boring Home Page', 'http://tomdoggett.net/'),
          ('LDS Subreddit', 'http://latterdaysaints.reddit.com'),
          ('Exmormon Subreddit', 'http://exmormon.reddit.com'),
          )

# Social widget
SOCIAL = (('Google+', 'https://plus.google.com/101615050717338574454'),
          ('Facebook', 'https://www.facebook.com/nocoolnametom'),
          ('Goodreads', 'http://www.goodreads.com/user/show/1508028-tom-doggett'),
          ('Bitcoin', 'bitcoin:1HDAy5n9qf3a7BtxxGoew6NwTAJ6BcBgrB'),
          )

DEFAULT_PAGINATION = 10

TAG_CLOUD_STEPS = 8

TAG_CLOUD_MAX_ITEMS = 100

if (settings.google_analytics):
  GOOGLE_ANALYTICS = settings.google_analytics

TWITTER_USERNAME = 'NoCoolName_Tom'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = (['admonition','extra','del_ins','superscript',])

TYPOGRIFY = True

PLUGINS = ['gravatar','pelican_youtube','social','microdata','pelican_alias']

GITHUB_URL = 'http://github.com/nocoolnametom/blog'

if (settings.disqus_sitename):
  DISQUS_SITENAME = settings.disqus_sitename

COLOPHON = True

COLOPHON_TITLE = u'Not a cool name,<br/>but at least a cool blog, right?'

COLOPHON_CONTENT = u'&nbsp;'