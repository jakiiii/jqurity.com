from django.db import models


# Create your models here.
class AyatModel(models.Model):
    ayat = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Ayat of Al-Quran"
