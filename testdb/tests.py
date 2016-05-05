# -*- coding: utf-8 -*-
import unittest
from datetime import datetime
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .models import Student, Group


class StudentTests(TestCase):

    def setUp(self):
        group1, created = Group.objects.get_or_create(title="QQ-1")
        Student.objects.get_or_create(first_name="СаШа", last_name="ШтО", birtday=datetime.today(), ticket='1231', student_group=group1)

        self.client = Client()

        self.url = reverse('home')


    #def setUp(self):
    #  Student.object.create(first_name="СаШа", last_name="ШтО", birtday="1999-12-12", ticket="1231", student_group="ЩЩ-11" )


    #def login_client_user(self):
    #    c = Client()
    #    response = c.post('/users/login/', {'username':'svo', 'passeord':'homoludens88'} )
    #    response.status_code

#class StudentTestCase(unittest.TestCase):

#    def setUp(self):
#        self.student = Student(first_name="СаШа", last_name="ШтО", birtday="1999-12-12", ticket="1231", student_group="ЩЩ-11")
#        self.student.save()
#
#    def tearDown(self):
#        self.student.delete()
#        self.student = None

#class StudentModelTests(TestCase):

#    def test_unicode(self):
#       student = Student(first_name='Demo', last_name='Student')
#        self.assertEqual(unicode(student), u'Demo Student')