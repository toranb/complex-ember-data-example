from os.path import dirname, join, abspath

try:                                                                                                                                                                                   
    from shlex import quote as shell_quote  # Python 3                                                                                                                                 
except ImportError:                                                                                                                                                                    
    from pipes import quote as shell_quote  # Python 2   

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
PROJECT_DIR = abspath(join(dirname(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_DIR, '..', 'codecamp.db'),
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = join(PROJECT_DIR, '..', 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.JSMinFilter',
)

STATICFILES_DIRS = (
    join(PROJECT_DIR, 'static'),
)

SECRET_KEY = 'x#9vlz4k1c4bh9ycy=6=bfze!8m&amp;)(^tpngqvfx_77z!_n=d-6'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'codecamp.urls'

WSGI_APPLICATION = 'codecamp.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'rest_framework',
    'codecamp.ember',
    'compressor',
)

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

NODE_ROOT = join(PROJECT_DIR, '..', 'node_modules')
HANDLEBARS_PATH = join(NODE_ROOT, 'django-ember-precompile', 'bin', 'django-ember-precompile')

# Escape characters in the file path (like spaces)
# Prevents django-compress manipulation errors 
HANDLEBARS_PATH = shell_quote(HANDLEBARS_PATH)

COMPRESS_PRECOMPILERS = (
    ('text/x-handlebars', '{} {{infile}}'.format(HANDLEBARS_PATH)),
)

REST_FRAMEWORK = {
    'FILTER_BACKEND': 'rest_framework.filters.DjangoFilterBackend'
}
