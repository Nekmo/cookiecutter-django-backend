from django.apps import AppConfig


class {{ cookiecutter.project_slug.title().replace('_', '') }}AppConfig(AppConfig):
    name = '{{ cookiecutter.project_slug }}'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from {{ cookiecutter.project_slug }} import celery  # noqa
