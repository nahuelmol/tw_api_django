from django.db import models

class theModel(models.Model):
	first_field = models.TextField()
	other_field = models.TextField()

class LaunchesSpaceX(models.Model):
	name = models.TextField()
	year_launch = models.IntegerField()
	launch_success = models.BooleanField(default=True)
	upcoming = models.BooleanField(default=False)
	launch_site = models.TextField()
	rocket_name = models.TextField()
	yt_video_link = models.CharField()
