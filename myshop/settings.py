
from pathlib import Path
import os
from django.contrib.messages import constants as messages



MESSAGE_TAGS = {
    messages.ERROR : 'danger',
    messages.INFO : 'success'
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'custom_loggin/static'),
    # os.path.join(BASE_DIR, 'products/static'),
    os.path.join(BASE_DIR, 'static')
    ]

STATIC_ROOT = os.path.join(BASE_DIR, 'allstatic')  # Dummy value for development

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gc*4=8c@3c=a84d(ub8gg1i4kbfxqhbyw2a*hga44ud_3xao*o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['5.253.24.73', 'www.taakkhaarid.ir']

# ---------------------------------Application definition------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangosecure',
    'csp',
    'background_task',
    'haystack',   
    'django_pdb',
    'custom_loggin',
    'products',
    'cart',
    'payments',
    'payment',
    'checkout',
    'rest_framework',
    'api',
    'rest_framework_swagger',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

CSRF_TRUSTED_ORIGINS = ['https://www.taakkhaarid.ir']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


#---------------------------------------------- Database---------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "db.sqlite3"),  # Use the default SQLite database
    }
}

#--------------------------------------- Password validation----------------------------------------

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


# ---------------------------------------Internationalization--------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = False


# -------------------------Static files (CSS, JavaScript, Images)------------------------------------

# STATIC_URL = '/static/'
# #STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


#----------------------------- Default primary key field type-------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#------------------------------------ https settings:----------------------------------------

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

#-----------------------------------Configure django-secure settings--------------------------

X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = False  
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_HSTS_SECONDS = 31536000  
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_REDIRECT_EXEMPT = []  

#-----------------------------------Configure CSP settings-----------------------------------

CSP_DEFAULT_SRC = ("'self'",)

#------------------------------------Enable cache and configure cache backend------------------

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        # Adjust this based on your Memcached server configuration.
        'LOCATION': '127.0.0.1:11211',  
    }
}

#-------------------------------------Payment backends------------------------------------

PAYMENT_BACKENDS = [
    'payments.backends.stripe.StripePayments',
]
#---
PAYMENT_HOST = 'example.com'
#---
PAYMENT_VARIANTS = {
    'default': ('payments.variants.StripePaymentsProvider', {
        'secret_key': 'your_stripe_secret_key',  # Replace with your Stripe secret key
        'public_key': 'your_stripe_public_key',  # Replace with your Stripe public key
        'store_name': 'Your Store Name',  # Replace with your store name
    }),
}

#----------------------------------------- Stripe API keys---------------------------------------------

STRIPE_PUBLIC_KEY = 'your_stripe_public_key'
STRIPE_SECRET_KEY = 'your_stripe_secret_key'

#-----------------------------------------------------

AUTH_USER_MODEL = 'custom_loggin.MyUser'

#--------------- authentication backend -----------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'custom_loggin.mybackend.ModelBackend',                     
]
#-------------------------------------------------------
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'images')

#-----------------------------------------------------

Kavenegar_API = '6550364A49313154626F717A544356532B71686A6550485A487A52573731344F7863797732416D513372633D'

#-------------------------------------------------------
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
        'URL': 'http://localhost:9200/',
        'INDEX_NAME': 'haystack',
    },
}
#----------------------------------------------------------
#SESSION

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_NAME = 'sessionid'
