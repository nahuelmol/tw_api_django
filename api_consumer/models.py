from django.db import models

class ClassName(models.Model):
	name = models.TextField()

class LaunchesSpaceX(models.Model):
	mission_name = models.TextField()
	launch_success = models.BooleanField(default=True)
	upcoming = models.BooleanField(default=False)
	launch_site = models.TextField()
	rocket_name = models.TextField()
	yt_video_link = models.CharField(max_length=25)
