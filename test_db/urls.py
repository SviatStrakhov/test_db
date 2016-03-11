"""test_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from testdb.views.students import StudentUpdateView, StudentDeleteView
from testdb.views.groups import GroupUpdateView, GroupDeleteView, groups_list, groups_add
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    # Groups urls
    url(r'^$', 'testdb.views.groups.groups_list', name='home'),
    url(r'^groups/add/$', login_required(groups_add), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', login_required(GroupUpdateView.as_view()), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', login_required(GroupDeleteView.as_view()), name='groups_delete'),


    # Students urls
    url(r'^students/$', 'testdb.views.students.students_list', name='students'),
    url(r'^students/add/$', 'testdb.views.students.students_add', name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

    # User Related urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page':'home'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),

    # Social Auth Related urls
    url('^social/', include('social.apps.django_app.urls', namespace='social')),



]



if DEBUG:
	# serve files from media folder
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}))
