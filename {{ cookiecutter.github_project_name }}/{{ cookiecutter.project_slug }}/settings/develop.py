from .defaults import *

ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, '_static')
MEDIA_ROOT = os.path.join(BASE_DIR, '_media')
DEBUG = True

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
