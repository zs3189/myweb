"""
Django settings for myweb project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
from myweb.config import LOCAL_DEBUG

import os, datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_z)80+tr(3b5zp^(y@do46u$ji@y5o=v!=#p72&7#g1cai@xk9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = LOCAL_DEBUG

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'bid',
    'images',
    'bbsapp',
    'forums',  # 论坛
    'account',
    'news',
    'crispy_forms',  # 美化form
    'django_extensions',
    'django_filters',
    'django_celery_results',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # 防跨站伪造请求
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

##权限控制
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # django默认的backend
    # 'guardian.backends.ObjectPermissionBackend',  #对对象的权限控制
)

ROOT_URLCONF = 'myweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'myweb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myweb',
        'USER': 'zs',
        'PASSWORD': 'Warzxw123;l',  # 最好从环境变量读取
        'HOST': '',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

##设置时区和语言
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
LOGIN_URL = '/account/login'
SITE_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

# 通用静态文件存放位置
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATICFILES_DIRS = (
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("js", os.path.join(STATIC_ROOT, 'js')),
    ("assets", os.path.join(STATIC_ROOT, 'assets'))
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media/')

APPEND_SLASH = True

# 自定义变量
UPLOAD_URL = '/upload'
UPLOAD_ROOT = os.path.join(BASE_DIR, 'upload/')
# 设置token过期时间
# REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES = 60 #60分钟过期
REST_FRAMEWORK = {
    # 使用Django的标准`django.contrib.auth`权限管理类,
    # 或者为尚未认证的用户，赋予只读权限.
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),

    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',  # 需要认证
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.AllowAny',
    ],
    # 分页
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 权限管理
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'app.myauth.CookieAuthentication',   #COKKIE认证
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'),
}
###JWT AUTH认证配置
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
        'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
        'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
        'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,  # 密钥
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',  # 加密算法    防止PAYLOAD被篡改 HEADER+PAYLOAD ->加密得到 signature
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),  # 过期时间
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    '''
    If JWT_ALLOW_REFRESH is True, non-expired tokens can be "refreshed" to 
    obtain a brand new token with renewed expiration time. 
    '''
    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),  #

    'JWT_AUTH_HEADER_PREFIX': 'JWT',  # headers 头  "Authorization: JWT your_token"
    'JWT_AUTH_COOKIE': None,

}

# 将SESSION改用Redis存储
# 设置 redis 缓存    key由前缀，版本号，真正的key组成
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# CACHES = {"default": {"BACKEND": "django_redis.cache.RedisCache",
#                       "LOCATION": "redis://127.0.0.1:6379/0",
#                             'OPTIONS': {
#             'DB': 0,
#             # 'PASSWORD': redis_url.password,
#             'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
#             'PICKLE_VERSION': -1,  # Use the latest protocol version
#             'SOCKET_TIMEOUT': 60,  # in seconds
#             'IGNORE_EXCEPTIONS': True,
#         }
#
#                       }
#           }

# SESSION设置   二选一生效
SESSION_COOKIE_AGE = 30 * 60  # 设置session过期时间为30分钟
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 会话cookie可以在用户浏览器中保持有效期。True：关闭浏览器，则Cookie失效  即过期时间为当前会话

'''配置session引擎SESSION_ENGINE为redis，配置此处session会存储在redis中，不会再去操作数据库了'''
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# 在登录函数中可以设置session有效期：request.session.set_expiry(30 * 60)


#
##django-crispy-forms  使用bootstrap
CRISPY_TEMPLATE_PACK = 'bootstrap3'

##--------------------------------------------------
##celery
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'django-cache'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}  # 1 hour.超时

##∂
##--------------------------------------------------
##配置邮箱
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = "smtp.qq.com"  # 服务器
EMAIL_PORT = 465  # 一般情况下都为25
EMAIL_HOST_USER = "810909753@qq.com"  # 账号
EMAIL_HOST_PASSWORD = "tveiryfnsgxibfia"  # 密码
EMAIL_SUBJECT_PREFIX = u'沪牌一号'  ##为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True
EMAIL_FROM = "810909753@qq.com"  # 邮箱来自

##--------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    # 'filters': {
    #     'special': {
    #         '()': 'project.logging.SpecialFilter',
    #         'foo': 'bar',
    #     },
    #     'require_debug_true': {
    #         '()': 'django.utils.log.RequireDebugTrue',
    #     },
    # },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        # 'file': {
        #     'level': 'DEBUG',
        #     'class': 'logging.FileHandler',
        #     'filename': 'mylog_test.log',
        #     'formatter': 'verbose'
        # },

        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler',
        #     'filters': ['special']
        # }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],  # console or file
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # For performance reasons, SQL logging is only enabled when settings.DEBUG is set to True
        # ref. https://docs.djangoproject.com/en/1.11/topics/logging/#django-db-backends
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        # 'api.views': {
        #     'handlers': ['console'],
        #     'propagate': False,
        #     'level': 'DEBUG',
        # },
        # 'background_task': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # }
        # 'myproject.custom': {
        #     'handlers': ['console', 'mail_admins'],
        #     'level': 'INFO',
        #     'filters': ['special']
        # }
    }
}

##-------------------------------------------------------------------
##设置上传大小
# Add to your settings file
CONTENT_TYPES = ['image', 'video']
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = 5242880
MAX_PHOTO_SIZE = 51200  ##头像50kb大小限制
