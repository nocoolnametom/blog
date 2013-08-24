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

THEME = "brownstone"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          )

# Social widget
SOCIAL = (('NoCoolName_Tom', 'http://gravatar.com/nocoolnametom'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = (['admonition','extra','del_ins','superscript',])

TYPOGRIFY = True

PLUGINS = ['gravatar','pelican_youtube','social','microdata','pelican_alias']
