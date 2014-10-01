from discuss.discuss.settings import *


##########################################################################
#
# Debug settings
#
##########################################################################
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG


##########################################################################
#
# Server settings
#
##########################################################################
ALLOWED_HOSTS = ["localhost"]

WSGI_APPLICATION = 'discuss.discuss.wsgi_development.application'
