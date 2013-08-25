#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.insert(0, '.')
from local import settings
sys.path.insert(0, settings.plugins_repo_path)

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = settings.publish_siteurl 
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

if (settings.publish_disqus_sitename):
  DISQUS_SITENAME = settings.publish_disqus_sitename

if (settings.publish_google_analytics):
  GOOGLE_ANALYTICS = settings.publish_google_analytics

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
