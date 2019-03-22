__version__ = "{{ cookiecutter.version }}"

default_app_config = '{{ cookiecutter.project_slug }}.apps.{{ cookiecutter.project_slug.title().replace('_', '') }}AppConfig'
