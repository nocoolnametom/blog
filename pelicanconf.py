#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.insert(0, '.')
from local import settings
sys.path.insert(0, settings.plugins_repo_path)

AUTHOR = u'NoCoolName Tom'
AUTHOR_EMAIL = u'nocoolnametom@gmail.com'
ABOUT = 'I\'m a programmer, Ancient Greek reader, feminist, spouse and partner, and a dad.'

SITENAME = u'NoCoolName Blog'
SITETAGLINE = u'Not a cool name, but at least a cool blog.'
SITEURL = settings.regular_siteurl
SITE_KEYWORDS = ['mormonism',
                 'religion',
                 'exmormon',
                 'bible',
                 'biblical scholarship',
                 'seminary',
                 'exegesis',
                 'history'
                ]

SITE_DESCRIPTION = ['This is my',
  'kinda-secret-but-not-so-secret-that-I\'m-going-to-be-neurotic-about-it blog detailing',
  'my thoughts as a disaffected Mormon (and pretty much anything else I decide to put',
  'here). I welcome discussion and even negative feedback, but this IS my blog and I\'ll',
  'not deal kindly with people trolling or just being morons.  All that aside, please',
  'enjoy yourselves and feel free to say what you think about my ramblings. :-)']


TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

HTML_LANG = 'en'

THEME = "lannisport"

ARCHIVES_URL = 'archives.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

HIDE_CATEGORIES_FROM_MENU = True

# Blogroll
LINKS_TITLE = 'Links'
LINKS =  (('My Technical Blog', 'http://blog.tomdoggett.net/'),
          #('Hire Me', 'http://tomdoggett.net/'),
          ('LDS Subreddit', 'http://latterdaysaints.reddit.com'),
          ('Exmormon Subreddit', 'http://exmormon.reddit.com'),
          )

# Social widget
SOCIAL_TITLE = 'Social'
SOCIAL = (#('google-plus', 'https://plus.google.com/101615050717338574454'),
          #('facebook', 'https://www.facebook.com/nocoolnametom'),
          #('goodreads', 'http://www.goodreads.com/user/show/1508028-tom-doggett'),
          #('twitter', 'https://twitter.com/NoCoolName_Tom'),
          #('github', 'https://github.com/nocoolnametom'),
          #('bitcoin', 'bitcoin:1HDAy5n9qf3a7BtxxGoew6NwTAJ6BcBgrB'),
          )

# Contact methods
CONTACTS = (('google-plus', 'https://plus.google.com/101615050717338574454'),
            ('facebook', 'https://www.facebook.com/nocoolnametom'),
            )

DEFAULT_PAGINATION = 10

TAG_CLOUD_STEPS = 8

TAG_CLOUD_MAX_ITEMS = 100

TWITTER_USERNAME = '@NoCoolName_Tom'
GITHUB_USERNAME = 'nocoolnametom'
GPLUS_USERNAME = '101615050717338574454'
GPLUS_API_ACCESS = 'AIzaSyCMGLkc4lz68Fu1ReF4m47wIDYAFZnimEE'

GITHUB_URL = 'https://github.com/nocoolnametom/blog'
TWITTER_URL = 'https://twitter.com/NoCoolName_Tom'
FACEBOOK_URL = 'https://www.facebook.com/nocoolnametom'
GOOGLE_URL = 'https://plus.google.com/101615050717338574454'
GOOGLEPLUS_URL = 'https://plus.google.com/101615050717338574454'
GOODREADS_URL = 'http://www.goodreads.com/user/show/1508028-tom-doggett'
BITCOIN_ADDRESS = '1HDAy5n9qf3a7BtxxGoew6NwTAJ6BcBgrB'

TWITTER_INTEGRATION_ENABLED = True

GOOGLE_PLUSONE = True
GPLUS_INTEGRATION_ENABLED = True

SITELOGO = 'avatar.png'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),
                 ('extra/favicon-195.png', 'static/avatar.png'),
                 ('extra/favicon-195.png', 'favicon-195.png'),
                 ('extra/favicon-152.png', 'favicon-152.png'),
                 ('extra/favicon-144.png', 'favicon-144.png'),
                 ('extra/favicon-128.png', 'favicon-128.png'),
                 ('extra/favicon-120.png', 'favicon-120.png'),
                 ('extra/favicon-114.png', 'favicon-114.png'),
                 ('extra/favicon-96.png', 'favicon-96.png'),
                 ('extra/favicon-72.png', 'favicon-72.png'),
                 ('extra/favicon-57.png', 'favicon-57.png'),
                 ('extra/favicon-32.png', 'favicon-32.png'),
                 ('extra/favicon.ico', 'favicon.ico'),
                 ('mt-tech-proposal.md', 'mt-tech-proposal.md'),
                 )

FAVICONS = {195: 'favicon-195.png',
            152: 'favicon-152.png',
            144: 'favicon-144.png',
            128: 'favicon-128.png',
            120: 'favicon-120.png',
            114: 'favicon-114.png',
            96:  'favicon-96.png',
            72:  'favicon-72.png',
            57:  'favicon-57.png',
            32:  'favicon-32.png',
            'ico': 'favicon.ico',
           }

MD_EXTENSIONS = (['admonition','extra','del_ins','superscript',])

TYPOGRIFY = True

PLUGINS = ['gravatar','pelican_youtube','social','microdata','pelican_alias']

# ARCHIVES_URL = ''
# CONTACT_URL = ''

if (settings.disqus_sitename):
  DISQUS_SITENAME = settings.disqus_sitename

if (settings.google_analytics):
  GOOGLE_ANALYTICS = settings.google_analytics
  GOOGLE_ANALYTICS_CODE = settings.google_analytics
  GOOGLE_ANALYTICS_ID = settings.google_analytics
  GOOGLE_ANALYTICS_SITENAME = settings.google_analytics_sitename

COLOPHON = True

COLOPHON_CONTENT = u'&nbsp;'

DISPLAY_HOME_ON_MENU = False

# Duplicate variables for avarious themes
SITE_KEYWORDS = ', '.join(SITE_KEYWORDS)
SITE_DESCRIPTION = ' '.join(SITE_DESCRIPTION)
CONTACT_EMAIL = AUTHOR_EMAIL
CONTACT = CONTACT_EMAIL
SITESUBTITLE = SITETAGLINE
SITEDESCR = SITE_DESCRIPTION
COLOPHON_TITLE = SITETAGLINE
