from django.db import models


# Create your models here.
class Experience(models.Model):
    experience = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.experience
