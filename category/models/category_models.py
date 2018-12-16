from django.db import models
from django.db.models.signals import pre_save

from jQurity.utils import unique_slug_generator


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.category

    @property
    def title(self):
        return self.category


def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_pre_save_receiver, sender=Category)
