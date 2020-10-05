"""
WSGI config for music project.

"""

import os
from django.core.wsgi import get_wsgi_application

import sys


sys.path.append('/var/www/music/')
os.environ["DJANGO_SETTINGS_MODULE"] = "music.settings"
application = get_wsgi_application()