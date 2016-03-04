# -*- coding: utf-8 -*-
from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, DeleteView
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from datetime import datetime
from . .models import Student, Group


# Views for Groups

def groups_add(request):
	if request.method == "POST":
		if request.POST.get('add_button') is not None:

			errors = {}

			data = {}

			title = request.POST.get('title', '').strip()
			if not title:
				errors['title'] = u"Номер групи є обов'язковим"
			else:
				data['title'] = title

			leader = request.POST.get('leader', '').strip()
			if not leader:
				errors['leader'] = u"Оберіть старосту"
			else:
				data['leader'] = Student.objects.get(pk=leader)

			if not errors:
				group = Group(**data)
				group.save()

				return HttpResponseRedirect(u'%s?status_message=Групу успішно додано!' % reverse('home'))
			else:
				return render(request, 'students/groups_add.html', {'students': Student.objects.all().order_by('last_name'), 'errors': errors})
		
		elif request.POST.get('cancel_button') is not None:
			return HttpResponseRedirect(u'%s?status_message=Додавання групи скасовано!' % reverse('home'))
	else:
		return render(request, 'students/groups_add.html', {'students': Student.objects.all().order_by('last_name')})


class GroupUpdateView(UpdateView):
	model = Group
	fields = '__all__'
	template_name = 'students/groups_edit.html'

	def get_success_url(self):
		return u'%s?status_message=Групу успішно збережено!' % reverse('home')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Редагування групи відмінено!' % reverse('home'))
		else:
			return super(GroupUpdateView, self).post(request, *args, **kwargs)



class GroupDeleteView(DeleteView):
	model = Group
	template_name = 'students/groups_confirm_delete.html'

	def get_success_url(self):
		return u'%s?status_message=Групу успішно видалено!' % reverse('home')

def groups_list(request):
	groups = Group.objects.all()

	# try to order students list
	order_by = request.GET.get('order_by', '')
	if order_by in ('title', 'leader'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()

	# paginate groups
	paginator = Paginator(groups, 3)
	page = request.GET.get('page')
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page
		groups = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results
		groups = paginator.page(paginator.num_pages)

	return render(request, 'students/groups_list.html', {'groups': groups})





