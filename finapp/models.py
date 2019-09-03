# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Fintab(models.Model):
	firstname=models.CharField(max_length=100)
	midname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	companyname=models.CharField(max_length=100)
	cityname=models.CharField(max_length=200)
	email=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	uname=models.CharField(max_length=100)
	psw=models.CharField(max_length=100)
	pswrpt=models.CharField(max_length=100)
	crd=models.CharField(max_length=25)
	protype=models.CharField(max_length=25,default="InvestPro")
	member=models.CharField(max_length=25,default="August 2019")
	

	def __str__(self):
		return '%s %s %s %s %s %s %s %s %s %s %s %s %s' %(self.firstname,self.midname,self.lastname,self.companyname,self.cityname,self.email,self.phone,self.uname,self.psw,self.pswrpt,self.crd,self.protype,self.member)
class UserTrack(models.Model):
	userid=models.IntegerField()
	act=models.CharField(max_length=100)
	track=models.DateTimeField(auto_now_add=True)

class Meta:
	db_table="fintab"
	db_table="usertrack"
	




