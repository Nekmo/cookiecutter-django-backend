{{ '#' * cookiecutter.project_name|length }}
{{cookiecutter.project_name}}
{{ '#' * cookiecutter.project_name|length }}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.github_project_name }}.svg?style=flat-square
  :target: https://pypi.org/project/{{ cookiecutter.github_project_name }}/
  :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.github_project_name }}.svg?style=flat-square
  :target: https://pypi.org/project/{{ cookiecutter.github_project_name }}/
  :alt: Python versions

.. image:: https://img.shields.io/codeclimate/maintainability/{{ cookiecutter.github_user }}/{{ cookiecutter.github_project_name }}.svg?style=flat-square
  :target: https://codeclimate.com/github/{{ cookiecutter.github_user }}/{{ cookiecutter.github_project_name }}
  :alt: Code Climate

.. image:: https://img.shields.io/codecov/c/github/{{ cookiecutter.github_user }}/{{ cookiecutter.github_project_name }}/master.svg?style=flat-square
  :target: https://codecov.io/github/{{ cookiecutter.github_user }}/{{ cookiecutter.github_project_name }}
  :alt: Test coverage

.. image:: https://img.shields.io/requires/github/{{ cookiecutter.github_user }}/{{ cookiecutter.github_project_name }}.svg?style=flat-square
  :target: https://requires.io/github/{{ cookiecutter.github_user }}/{{ cookiecutter.github_project_name }}/requirements/?branch=master
  :alt: Requirements Status


{{cookiecutter.description}}

Development commands
====================

Type checks
-----------

Running type checks with mypy::

  $ mypy {{ cookiecutter.project_slug }}


Test coverage
-------------

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html


Celery
------

This app comes with Celery. To run a celery worker:

.. code-block:: bash

    celery -A {{ cookiecutter.project_slug }} worker -l info
