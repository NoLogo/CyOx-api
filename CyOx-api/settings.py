import mimetypes
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
import django_cache_url
import dj_database_url

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(PROJECT_DIR)

ALLOWED_HOSTS = ['*']

DEBUG = bool(os.environ.get('DEBUG', False))
DEVELOPMENT_SITE = bool(os.environ.get('DEVELOPMENT_SITE', False))

DATABASES = {'default': dj_database_url.config(default='postgres://localhost/cyox')}

CACHES = {'default': django_cache_url.config()}

ADMINS = ()
MANAGERS = ADMINS

TIME_ZONE = 'UTC'
USE_L10N = True  # Locale
USE_TZ = True

LANGUAGE_CODE = 'en-GB'
USE_I18N = False  # Internationalization

# Time Format
TIME_INPUT_FORMATS = ('%m/%d/%y - %I:%M %p',)

# Static
MEDIA_ROOT = os.path.join(ROOT_DIR, 'client_media')
MEDIA_URL = '/client_media/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'static_media')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

CSS_DEBUG = os.environ.get('CSS_DEBUG', False)

mimetypes.add_type('text/x-component', '.htc')

TEMPLATE_DEBUG = DEBUG
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# Make this unique, and don't share it with anybody.

ROOT_URLCONF = 'CyOx-api.urls'
SECRET_KEY = 'u+m!cje0y@ais%rqn)##@h_220f56_q!x*vt)gjt2v67g5@22u'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SITE_ID = 1
WSGI_APPLICATION = 'CyOx-api.wsgi.application'

INSTALLED_APPS = (
    'CyOx-api',

    'rest_framework',
    'south',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

# A sample logging configuration. The only tangible logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Debug Toolbar
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
INTERNAL_IPS = ('127.0.0.1',)
