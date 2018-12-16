from django.db import models


# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=32)
    subject = models.CharField(max_length=120)
    context = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
