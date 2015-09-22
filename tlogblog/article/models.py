from django.db import models
from time import time

def get_upload_file_name(instance,filename):
    return "upload_files/%s_%s" % (str(time()).replace('.','_'),filename)

# Create your models here.
class Article(models.Model):
	author = models.CharField(max_length = 50, blank = True)
	title = models.CharField(max_length = 200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	thumbnail = models.FileField(upload_to=get_upload_file_name, blank = True)  

	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return "/articles/get/%i/" % self.id
	
	def get_thumbnail(self):
		thumb = str(self.thumbnail)
		if not settings.DEBUG:
			thumb = thumb.replace('assets/', '')

		return thumb


class Comment(models.Model):
    name = models.CharField(max_length = 200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    article = models.ForeignKey(Article)


class Quote(models.Model):
	title = models.CharField(max_length = 25)
	body = models.TextField()

