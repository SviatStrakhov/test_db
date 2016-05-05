# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
	"""Student Model"""


	class Meta(object):
		verbose_name = u"Студент"
		verbose_name_plural = u"Студенти"

			

	first_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім'я")

	last_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Прізвище")

	middle_name = models.CharField(
		max_length=256,
		blank=True,
		verbose_name=u"По-батькові",
		default='')

	birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата народження",
        null=True)

	photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True)

	student_group = models.ForeignKey('Group',
		verbose_name=u"Група",
		blank=False,
		null=True,
		on_delete=models.PROTECT)

	ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Білет")

	notes = models.TextField(
        blank=True,
		verbose_name=u"Додаткові нотатки")

	def __unicode__(self):
		return u"%s %s" % (self.last_name, self.first_name)


class Group(models.Model):
	"""Group Model"""
	

	class Meta(object):
		verbose_name = u"Група"
		verbose_name_plural = u"Групи"

			

	title = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u"Назва")

	leader = models.OneToOneField('Student',
		verbose_name=u"Староста",
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	notes = models.TextField(
        blank=True,
		verbose_name=u"Додаткові нотатки")

	def __unicode__(self):
		return u"%s (%s %s)" % (self.title, self.leader.last_name, self.leader.first_name)

