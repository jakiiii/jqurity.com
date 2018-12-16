from django.db import models


# Create your models here.
class SocialModel(models.Model):
    facebook = models.URLField(max_length=150, null=True, blank=True)
    twitter = models.URLField(max_length=150, null=True, blank=True)
    linkedin = models.URLField(max_length=150, null=True, blank=True)
    github = models.URLField(max_length=150, null=True, blank=True)
    gitlab = models.URLField(max_length=150, null=True, blank=True)
    hackerrank = models.URLField(max_length=150, null=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Social Links"
