from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chathistory(models.Model):
	userid = models.IntegerField(null=True)
	senderid = models.IntegerField()
	receiverid = models.IntegerField()
	message = models.CharField(max_length=300)
	time = models.DateTimeField(auto_now_add=True,null=True)


class Chatbuffer(models.Model):
	userid = models.IntegerField(null=True)
	senderid = models.IntegerField()
	receiverid = models.IntegerField()
	message = models.CharField(max_length=300)
	time = models.DateTimeField(auto_now_add=True,null=True)

class Onlineusers(models.Model):
	olu = models.ForeignKey(User )