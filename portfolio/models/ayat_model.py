from django.db import models


# Create your models here.
class Ayat(models.Model):
    ayat = models.TextField()
    verse = models.CharField(max_length=120)
    verse_link = models.URLField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.verse
