# -*- coding: utf-8 -*-
# Copyright: See the LICENSE file.

"""Settings for factory_boy/Django tests."""

import os

FACTORY_ROOT = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),     # /path/to/fboy/tests/djapp/
    os.pardir,                                      # /path/to/fboy/tests/
    os.pardir,                                      # /path/to/fboy
)

MEDIA_ROOT = os.path.join(FACTORY_ROOT, 'tmp_test')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
    'replica': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'tests.djapp'
]

MIDDLEWARE_CLASSES = ()

SECRET_KEY = 'testing.'
