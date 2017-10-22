# -*- coding: utf-8 -*-
 
from .models import Home,Program,Technology,About
from django.shortcuts import render  
from django.contrib.auth import logout
from django.http import HttpResponseRedirect,HttpResponse



def index(request):
	indexx = Home.objects.filter()
	return render(request,'default/index.html',locals())


def programs(request):
	programss=Program.objects.filter()
	return render(request,'default/programs.html',locals())

def technologies(request):
	technology=Technology.objects.filter()
	return render(request,'default/technologies.html',locals())

def about(request):
	try:
		aboutt = About.objects.first()
		return render(request,'default/about.html',locals())
	except Exception:
		return render(request,'default/404.html',locals())

def logoutt(request):
	b = request.user.id
	if (not b):
		return HttpResponseRedirect('/home')
	logout(request)
	return HttpResponse("Cikis yapildi")

def design(request):
	b = request.user.id
	if (not b):
		return HttpResponseRedirect('/login')
	return HttpResponseRedirect('/admin/app/')

