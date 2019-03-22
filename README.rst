
Cookiecutter Django Backend
###########################


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
