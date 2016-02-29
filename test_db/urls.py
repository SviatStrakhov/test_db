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

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    # Groups urls
    url(r'^$', 'testdb.views.groups.groups_list', name='home'),
    url(r'^groups/add/$', 'testdb.views.groups.groups_add', name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$','testdb.views.groups.groups_edit', name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', 'testdb.views.groups.groups_delete', name='groups_delete'),


    	# Students urls
    url(r'^students/$', 'testdb.views.students.students_list', name='students'),
    url(r'^students/add/$', 'testdb.views.students.students_add', name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', 'testdb.views.students.students_edit', name='students_edit'),
   	url(r'^students/(?P<sid>\d+)/delete/$', 'testdb.views.students.students_delete', name='students_delete'),


]

from .settings import MEDIA_ROOT, DEBUG

if DEBUG:
	# serve files from media folder
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}))