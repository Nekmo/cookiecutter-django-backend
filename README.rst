.. image:: https://raw.githubusercontent.com/Nekmo/cookiecutter-django-backend/master/images/logo.png
    :width: 100%

|

.. image:: https://img.shields.io/pypi/v/cookiecutter-django-backend.svg?style=flat-square
  :target: https://pypi.org/project/cookiecutter-django-backend/
  :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/pyversions/cookiecutter-django-backend.svg?style=flat-square
  :target: https://pypi.org/project/cookiecutter-django-backend/
  :alt: Python versions

.. image:: https://img.shields.io/requires/github/Nekmo/cookiecutter-django-backend.svg?style=flat-square
     :target: https://requires.io/github/Nekmo/cookiecutter-django-backend/requirements/?branch=master
     :alt: Requirements Status


Cookiecutter Django Backend
###########################
A cookiecutter for create a simple and standard Django project with everything necessary for a backend. Unlike other
cookiecutters, it is less intrusive.

Install or update Cookiecutter to the latest version::

    $ pip install -U cookiecutter

Create your new project using this cookiecutter::

    $ cookiecutter https://github.com/Nekmo/cookiecutter-django-backend.git

Or use the abbreviation (see below)::

    $ cookiecutter dj

This cookiecutter is based on `cookiecutter-django <https://github.com/pydanny/cookiecutter-django>`_, but
the structure is standard and simpler.

Features
========

* For Django 2.0+
* Docker support using docker-compose.
* Secure by default. With HTTPS Nginx config and Let'sEncrypt.
* Develop and production settings
* Ready for Celery and Django Rest Framework.
* Deployment using Ansible and Docker.


Customize your default options
==============================
There are certain options that are always repeated every time cookiecutter is executed. Create a ``.cookiecutterrc``
file in your user directory:

.. code-block:: yaml

    default_context:
      author_name: Nekmo
      github_user: Nekmo
      email: myemail@nekmo.com
      open_source_license: MIT
      timezone: Europe/Madrid
    abbreviations:
      dj: https://github.com/Nekmo/cookiecutter-django-backend
      gh: https://github.com/{0}.git

