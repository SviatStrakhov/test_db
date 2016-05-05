# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Student, Group
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError


class StudentInline(admin.StackedInline):
	model = Student

class GroupAdmin(admin.ModelAdmin):
	inlines = [
		StudentInline,
	]



# Register your models here.
admin.site.register(Student)
admin.site.register(Group)

