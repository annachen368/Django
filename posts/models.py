from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120) # character CharField max_length=120
	content = models.TextField() # longer then char TextField
	updated = models.DateTimeField(auto_now=True, auto_now_add=False) # 
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True) # auto_now: everytime update db/auto_now_add: first time add and update db

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id":self.id})