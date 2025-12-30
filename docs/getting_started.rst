Getting Started
===============

Requirements
------------

* **Django**: 5.0, 5.1+
* **Python**: 3.11, 3.12, 3.13+

.. note:: For Django < 5.0, please use Django Suit 0.2.x (``pip install django-suit==0.2.28``)

Installation
------------


1. You can get stable version of Django Suit by using pip or easy_install::

    pip install django-suit==0.3.0

2. You will need to add the ``'suit'`` application to the ``INSTALLED_APPS`` setting of your Django project ``settings.py`` file.::

    INSTALLED_APPS = (
        ...
        'suit',
        'django.contrib.admin',
    )

  .. important:: ``'suit'`` must be added before ``'django.contrib.admin'`` and if you are using third-party apps with special admin support (like django-cms) you also need to add ``'suit'`` before ``'cms'``.

3. Make sure you have ``django.template.context_processors.request`` in your ``TEMPLATES`` ``OPTIONS`` ``context_processors`` setting in your Django project ``settings.py`` file.::


      TEMPLATES = [
          {
              'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [],
              'APP_DIRS': True,
              'OPTIONS': {
                  'context_processors': [
                      'django.template.context_processors.debug',
                      'django.template.context_processors.request', # Make sure you have this line
                      'django.contrib.auth.context_processors.auth',
                      'django.contrib.messages.context_processors.messages',
                  ],
              },
          },
      ]


  Note: This is required to handle left side menu. If by some reason you removed original Django Suit ``menu.html``, you can skip this.


Deployment
----------

Deployment with Django Suit should not be different than any other Django application. If you have problems with deployment on production, read `Django docs on wsgi <https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/>`_ first.

.. note:: If you deploy your project with Apache or ``Debug=False`` don't forget to run ``./manage.py collectstatic``


Develop branch
--------------

`Develop branch <https://github.com/darklow/django-suit/commits/develop>`_ is considered as release candidate version. Check `commits <https://github.com/darklow/django-suit/commits/develop>`_ and `changelog <https://github.com/darklow/django-suit/blob/develop/CHANGELOG.rst>`_ of develop branch first, before installing develop version. It is quite stable and always tested, but can contain some flaws or behaviour changes too. To install latest develop version use::

  pip uninstall django-suit
  pip install https://github.com/darklow/django-suit/tarball/develop


v2-dev branch
-------------

`v2-dev branch <https://github.com/darklow/django-suit/issues/475>`_ is a complete rewrite using Bootstrap v4. It is still in development and this documentation doesn't match v2-dev. Read more about v2 `here <https://github.com/darklow/django-suit/issues/475>`_. To install latest v2 version use::

  pip uninstall django-suit
  pip install https://github.com/darklow/django-suit/tarball/v2

