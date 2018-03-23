import dj_database_url
from decouple import Csv, config
from unipath import Path
import os


PROJECT_DIR = Path(__file__).parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

#ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
ALLOWED_HOSTS=['172.16.0.40:8000']
# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.sites',

    #'django_python3_ldap',
    #'ldap_sync',
    #'wiki',
    #'bootcamp.wiki.plugins.macros',
    #'bootcamp.wiki.plugins.help',
    #'bootcamp.wiki.plugins.links',
    #'bootcamp.wiki.plugins.images',
    #'bootcamp.wiki.plugins.attachments',
    #'bootcamp.wiki.plugins.notifications',
    #'bootcamp.wiki.plugins.globalhistory',
    'sekizai',
    'sorl.thumbnail',
    'django_nyt',
    'mptt',

    'bootcamp.authentificate',
    'bootcamp.multimedia',
    'bootcamp.activities',
    'bootcamp.articles',
    'bootcamp.authentication',
    'bootcamp.core',
    'bootcamp.feeds',
    'bootcamp.messenger',
    'bootcamp.questions',
    'bootcamp.search',
    'taggit',
    'embed_video',  
    'gunicorn',  
)
SITE_ID = 1
# AUTH_USER_MODEL = 'authentificate.CustomUser'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ROOT_URLCONF = 'bootcamp.urls'

WSGI_APPLICATION = 'bootcamp.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_DIR.child('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "sekizai.context_processors.sekizai",
            ],
            'debug': DEBUG
        },
    },
]

# import ldap3
# from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

AUTHENTICATION_BACKENDS = [
    #'django_python3_ldap.auth.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
]
# The URL of the LDAP server.
LDAP_AUTH_URL = "ldap://dc.feicom.cm:389"
LDAP_AUTH_CONNECTION_USERNAME = "FEICOMDG\\administrateur"
LDAP_AUTH_CONNECTION_PASSWORD = "CSID-feicom@2016"
# Initiate TLS on connection.
LDAP_AUTH_USE_TLS = False

# The LDAP search base for looking up users.
LDAP_AUTH_SEARCH_BASE = "OU=FEICOM,DC=feicom,DC=cm"

# The LDAP class that represents a user.
LDAP_AUTH_OBJECT_CLASS = "Person"

# User model fields mapped to the LDAP
# attributes that represent them.
LDAP_AUTH_USER_FIELDS = {
    "username": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "userPrincipalName",
}

# A tuple of django model fields used to uniquely identify a user.
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)


# Path to a callable that takes a dict of {model_field_name: value},
# returning a dict of clean model data.
# Use this to customize how data loaded from LDAP is saved to the User model.
#LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"

# Path to a callable that takes a user model and a dict of {ldap_field_name: [value]},
# and saves any additional user relationships based on the LDAP data.
# Use this to customize how data loaded from LDAP is saved to User model relations.
# For customizing non-related User model fields, use LDAP_AUTH_CLEAN_USER_DATA.
#"LDAP_AUTH_SYNC_USER_RELATIONS = "django_python3_ldap.utils.sync_user_relations"

# Path to a callable that takes a dict of {ldap_field_name: value},
# returning a list of [ldap_search_filter]. The search filters will then be AND'd
# together when creating the final search filter.
#LDAP_AUTH_FORMAT_SEARCH_FILTERS = "django_python3_ldap.utils.format_search_filters"

# Path to a callable that takes a dict of {model_field_name: value}, and returns
# a string of the username to bind to the LDAP server.
# Use this to support different types of LDAP server.
#LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_openldap"

# Sets the login domain for Active Directory users.
# LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = "u:FEICOMDG\""

# The LDAP username and password of a user for querying the LDAP database for user
# details. If None, then the authenticated user will be used for querying, and
# the `ldap_sync_users` command will perform an anonymous query.
# LDAP_AUTH_CONNECTION_USERNAME = None
# LDAP_AUTH_CONNECTION_PASSWORD = None

# Set connection/receive timeouts (in seconds) on the underlying `ldap3` library.
LDAP_AUTH_CONNECT_TIMEOUT = None
LDAP_AUTH_RECEIVE_TIMEOUT = None


# AUTH_LDAP_SERVER_URI = "ldap://dc.feicom.cm"
# AUTH_LDAP_BIND_DN = "l.taboua@feicom.cm"
# AUTH_LDAP_BIND_PASSWORD = "123mauricephone@gmail.com"
# AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=feicom,dc=cm",
#     "(objectClass=groupOfNames)"
# )
# AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()


HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_DIR, 'index_woosh')

# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
#     },
# }


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'xapian_backend.XapianEngine',
        'PATH': os.path.join(PROJECT_DIR, 'xapian_index'),
    },
}


for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    import debug_toolbar  # @UnusedImport
    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES) + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INSTALLED_APPS = list(INSTALLED_APPS) + ['debug_toolbar']
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
except ImportError:
    pass

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('pt-br', 'Portuguese'),
    ('es', 'Spanish'),
    ('zh-cn', 'Chinese'),
)

LOCALE_PATHS = (PROJECT_DIR.child('locale'), )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = PROJECT_DIR.parent.child('staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

MEDIA_ROOT = PROJECT_DIR.parent.child('media')
MEDIA_URL = '/media/'

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/feeds/'

ALLOWED_SIGNUP_DOMAINS = ['*']

FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0o644

TAGGIT_CASE_INSENSITIVE = True

WIKI_ANONYMOUS_WRITE = True
WIKI_ANONYMOUS_CREATE = False
