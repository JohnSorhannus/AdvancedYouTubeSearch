from django.db import models

# Create your models here.
class Video(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	upload_date = models.CharField(max_length=10)
	user = models.CharField(max_length=200)
	captions = models.TextField(null=True) #some videos may not contain captions
	thumbnail_url = models.TextField()
	video_url = models.TextField()
	length = models.CharField(max_length=200)
	views = models.CharField(max_length=200)

	def __str__(self):
		return self.title

