from discuss.discuss.settings import *


##########################################################################
#
# Server settings
#
##########################################################################
ALLOWED_HOSTS = []

WSGI_APPLICATION = 'discuss.discuss.wsgi_production.application'


##########################################################################
#
# Database settings
#
##########################################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_DIR, 'db', 'production_db.sqlite3'),
    }
}
