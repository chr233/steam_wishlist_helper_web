"""
Django settings for swhweb project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '#z=hi9id^b^)_*wdein24mv$bq+lwbr7rr287xw)xdzx%qmyk$'

DEBUG = False

ALLOWED_HOSTS = ['swh.chrxw.cn', '127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_crontab',
    'rest_framework',

    'app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
        'rest_framework.authtoken'
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'swhweb.urls'

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

WSGI_APPLICATION = 'swhweb.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

SWH_SETTINGS = {
    # ITAD Token
    'ITAD_TOKENS': (
        '',
        '',
        '',
        '',
    ),
    # 商店信息更新频率(秒)
    'INFO_UPDATE_PERIOD': 10 * 86400,
    # 价格信息更新频率(秒)
    'PRICE_UPDATE_PERIOD': 1 * 86400,
    # 更新时间递减量(秒)
    'TIME_DECREASE': 30,
    # 一次添加新游戏的数量(太多可能会被banIP)
    'NEW_GAME_AMOUNT': 50,
    # 一次更新旧游戏的数量(太多可能会被banIP)
    'OLD_GAME_AMOUNT': 50,
    # 出错自动禁用阈值,错误次数达到后自动禁用更新
    'MAX_ERROR': 1,
    # 地区(影响价格)
    'REGION': 'cn',
    # 国家(影响价格)
    'COUNTRY': 'CN',
}

CRONJOBS = [
    ('*/1 * * * *', 'app.task.add_new', f'>> {BASE_DIR}/tasks.log'),
    ('*/4 * * * *', 'app.task.flush_current', f'>> {BASE_DIR}/tasks.log')
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    #   'DEFAULT_THROTTLE_RATES':{          #继承节流组件的SimpleRateThrottle类使用
    #     'ThrottleTest':'5/m',#该key是在自定义的组件类定义的，value值形如：'5/s'或者'5/seconds'均可（只要是以s,m,h,d即可）
    #     #'LoginedUser':'10/m',#可以针对不懂得身份标识进行节流规则制定
    # },
}

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'