# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
	kullanici = models.ForeignKey(User)
	baslik = models.CharField(max_length=64)
	text = models.TextField()
	tarih = models.DateTimeField('date_published')

	def __str__(self):
		return self.baslik

class Program(models.Model):
	kullanici = models.ForeignKey(User)
	baslik = models.CharField(max_length=64)
	text = models.TextField()
	tarih = models.DateTimeField('date_published')

	def __str__(self):
		return self.baslik

class About(models.Model):
	isim = models.CharField(max_length=32)
	soy_isim = models.CharField(max_length=32,default='')
	bolum = models.CharField(max_length=64)
	tel = models.CharField(max_length=32)
	adres = models.CharField(max_length=128)
	foto = models.FileField(upload_to='static/documents/%Y/%m/%d')

	def __str__(self):
		return self.isim

class Technology(models.Model):
	kullanici = models.ForeignKey(User)
	baslik = models.CharField(max_length=64)
	text = models.TextField()
	tarih = models.DateTimeField('date_published')

	def __str__(self):
		return self.baslik


