# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class TestdbAppConfig(AppConfig):
    name = 'testdb'
    verbose_name = u'База Студентів'

    def ready(self):
        from testdb import signals
