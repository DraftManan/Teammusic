from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0frz@323m&l!v*ytn(gm-l&&$n)ne#mz7=ewx4^v37%jxs%pns'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['3.89.155.209', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'tailwind',
    'theme',
    'django_browser_reload',
    'music',

]

TAILWIND_APP_NAME = 'theme'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    'music.middleware.CognitoLoginRequiredMiddleware',

]

ROOT_URLCONF = 'teammusic.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'teammusic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',       # ใช้ PostgreSQL
        'NAME': 'teammusic',                          # ชื่อฐานข้อมูลใน RDS
        'USER': 'postgres',                          # ชื่อผู้ใช้ฐานข้อมูล
        'PASSWORD': env('DB_PASSWORD'),                  # รหัสผ่านผู้ใช้
        'HOST': 'dbteammusic.cnuqpvfxepaj.us-east-1.rds.amazonaws.com',  # Endpoint ของ RDS instance
        'PORT': '5432',                                  # พอร์ตของ PostgreSQL (ค่าเริ่มต้นคือ 5432)
    }
}


# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'rediss://teammusiccache-ntfgri.serverless.use1.cache.amazonaws.com:6379/1',  # ใช้ endpoint ของ ElastiCache
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


COGNITO_REGION = 'us-east-1'

LOGIN_URL = '/teammusic/signin'


# ตั้งค่าตัวแปร AWS และ Cognito
AWS_REGION_NAME = env('AWS_REGION_NAME')
COGNITO_USER_POOL_ID = env('COGNITO_USER_POOL_ID')
COGNITO_IDENTITY_POOL_ID = env('COGNITO_IDENTITY_POOL_ID')
COGNITO_CLIENT_ID = env('COGNITO_CLIENT_ID')

MEDIA_URL = '/img/'  # URL ที่จะใช้ในการเข้าถึงไฟล์ใน media
MEDIA_ROOT = os.path.join(BASE_DIR, 'img')  # พาธของโฟลเดอร์ที่เก็บไฟล์จริงๆ