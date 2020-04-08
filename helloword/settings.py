"""
Django settings for helloword project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2__n!4^zb1n=f(0+3xkbrask0(2n(#8-9h!-kcixn#x3+=+2++'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 自己的app的apps的文件里的类
    'app1.apps.App1Config',
    'blog.apps.BlogConfig',
    'juheapp.apps.JuheappConfig',
    'django_crontab'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'mymiddleware.mymiddleware.TestMiddle',
    # 'mymiddleware.mymiddleware.StatisticsMiddle',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

APPEND_SLASH = False

ROOT_URLCONF = 'helloword.urls'

UPLOAD_PIC_DIR = os.path.join(BASE_DIR, 'resource', 'uploadpic')

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

WSGI_APPLICATION = 'helloword.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
#     # 从数据库
#     'slave': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'test',
#         'USER': 'root',
#         'PASSWORD': '258000',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': '258000',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
os.environ['DJANGO_SETTINGS_MODULE'] = 'helloword.settings'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
)
# print('STATICFILES_DIRS:',STATICFILES_DIRS)
STATIC_ROOT_SELF = os.path.join(BASE_DIR, 'static')

# SESSION_COOKIE_AGE session 过期时间
SESSION_COOKIE_AGE = 60 * 1 * 24

# 日志
LOGGING = {
    'version': 1,
    # 格式器
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s: %(thread)d]'
                      '%(pathname)s:%(funcName)s:%(lineno)d %(levelname)s - %(message)s'
        },
        'myformat': {
            'format': '%(asctime)s '
                      '%(pathname)s:%(funcName)s:%(lineno)d %(levelname)s - %(message)s'

        }
    },
    # 过滤器
    'filters': {
        'xxx': {
            '()': 'ops.XXXFilter'
        }
    },
    'handlers': {
        #     控制台输出
        'consile_handler': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出到文件
        'file_handler': {
            # DEBUG  Warning ERROR
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            # todo  可能日志不存在
            'filename': os.path.join(BASE_DIR, 'ops.log'),
            'maxBytes': 100 * 1024 * 1024,
            'backupCount': 3,
            'formatter': 'standard',
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['consile_handler', 'file_handler'],
            'filters': ['xxx'],
            'level': 'DEBUG'
        }
    },
}

# 缓存模块
CACHES = {
    'default': {
        # 框架缓存
        # 1. MemCache
        # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'LOCATION': '127.0.0.1:11211',

        # 2. DB Cache
        # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        # 'LOCATION': 'my_cache_table',

        # 3. Filesystem Cache
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'LOCATION': '/var/tmp/django_cache',

        # 4. Local Mem Cache
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'backend-cache'
    }
}

# crontab常见与linux和unix

CRONJOBS = [
    ('*/2 * * * *', 'corn.jobs.demo'),
    ('*/1 * * * *', 'echo "xxx">/dev/null')
    # ('*/3 * * * *', '/bin/ls'),
]
