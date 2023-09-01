from .defaults import *

ALLOWED_HOSTS = ['*']
STATIC_ROOT = str(BASE_DIR / '_static')
MEDIA_ROOT = str(BASE_DIR / '_media')
DEBUG = True


{% if cookiecutter.use_postgres_in_dev %}
def get_docker_container_ip(container_name):
    from subprocess import check_output
    {% raw %}
    output = check_output(['docker', 'inspect',
                           '-f', '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}', container_name])
    {% endraw %}
    return output.decode('utf-8').strip()


DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'postgres',
    'USER': 'postgres',
    'HOST': get_docker_container_ip('{{ cookiecutter.repo_project_name }}!!DOCKER_SEPARATOR!!postgres!!DOCKER_SEPARATOR!!1'),
    'PORT': '',
    'PASSWORD': 'postgres',
}
{% else %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}{% endif %}


EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
