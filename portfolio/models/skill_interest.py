from django.db import models


# Create your models here.
class Interest(models.Model):
    interest = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.interest
