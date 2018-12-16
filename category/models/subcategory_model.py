from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save

from .category_models import Category

from jQurity.utils import unique_slug_generator


# Create your models here.
class SubCategory(models.Model):
    sub_category = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.sub_category

    @property
    def title(self):
        return self.sub_category

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})


def sub_category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(sub_category_pre_save_receiver, sender=SubCategory)
