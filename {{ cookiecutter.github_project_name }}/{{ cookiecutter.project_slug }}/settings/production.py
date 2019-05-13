import raven
from .defaults import *

ALLOWED_HOSTS = ['{{ cookiecutter.domain_name }}']

STATIC_ROOT = '/static'
MEDIA_ROOT = '/media'

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'postgres',
    'USER': 'postgres',
    'HOST': '',
    'PORT': '',
    'PASSWORD': '',
    'CONN_MAX_AGE': 180,
}

# CACHES
# ------------------------------------------------------------------------------
CACHES['default'] = {
    'BACKEND': 'redis_cache.RedisCache',
    'LOCATION': '',
    'TIMEOUT': 60,
    'OPTIONS': {
        'DB': 0,
        'MAX_ENTRIES': 10000,
        "CLIENT_CLASS": "django_redis.client.DefaultClient",
        "IGNORE_EXCEPTIONS": True,
    }
}

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[0]["OPTIONS"]["loaders"] = [
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]
del TEMPLATES[0]['APP_DIRS']

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = "{{cookiecutter.project_name}} <noreply@{{cookiecutter.domain_name}}>"
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = DEFAULT_FROM_EMAIL
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = default="[{{cookiecutter.project_name}}]"

# SENTRY VALIDATION
# ------------------------------------------------------------------------------
RAVEN_CONFIG = {
    'dsn': '',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(BASE_DIR),
}

# LOGGING
# ------------------------------------------------------------------------------
ROTATING_FILE_HANDLER = {
    'class': 'logging.handlers.RotatingFileHandler',
    'maxBytes': 1024 * 1024 * 50,  # 50MB
    'backupCount': 10,
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': RAVEN_CONFIG['dsn'],
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            "stream": "ext://sys.stdout"
        },
        'celery_file': dict(ROTATING_FILE_HANDLER, **{
            'level': 'INFO',
            'filename': os.path.join(LOGS_DIRECTORY, 'celery.log'),
        }),
        'info_file': dict(ROTATING_FILE_HANDLER, **{
            'level': 'INFO',
            'filename': os.path.join(LOGS_DIRECTORY, 'info.log'),
        }),
        'error_file': dict(ROTATING_FILE_HANDLER, **{
            'level': 'ERROR',
            'filename': os.path.join(LOGS_DIRECTORY, 'error.log'),
        }),
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        '': {
            'handlers': ['info_file', 'console', 'sentry'],
            'level': 'INFO',
            'propagate': False,
        },
        'celery': {
            'handlers': ['celery_file', 'sentry'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['info_file', 'error_file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['error_file', 'mail_admins'],
            'propagate': False,
        },
    }
}
LOGGING['loggers']['sentry.errors'] = LOGGING['loggers']['raven']


# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = True
