from django.conf.urls import url
from django.contrib import admin
from app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^home/', views.index),
	url(r'^admin/', admin.site.urls),
	url(r'^technologies/', views.technologies),
    url(r'^programs/', views.programs),
    url(r'^about/', views.about),
    url(r'^design/', views.design),
    url(r'^logout/', views.logoutt),
    url(r'^login', auth_views.login, {'template_name': 'default/login.html'}),
]
