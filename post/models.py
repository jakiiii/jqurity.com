import os
import random

from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save
from django.core.files.storage import FileSystemStorage

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from category.models import Category, SubCategory
from tags.models import Tag

from jQurity.utils import unique_slug_generator
fs = FileSystemStorage(location='media')


def get_filename_exist(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(inistance, file_name):
    new_filename = random.randint(1, 101119)
    name, ext = get_filename_exist(file_name)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "blog/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


User = settings.AUTH_USER_MODEL


# Create your queryset here.
class PostQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__tag__icontains=query))
        return self.active().filter(lookups).distinct()  # distinct is ignore multiple value

    def category(self, category_slug):
        return Post.objects.filter(category__sub_category__iexact=category_slug)


# Create your manager here.
class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def search(self, query):
        return self.get_queryset().search(query)

    def category(self, category_slug):
        return self.get_queryset().category(category_slug)


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    link = models.URLField(max_length=300, null=True, blank=True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, unique=True)

    objects = PostManager()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})

    def get_absolute_update_url(self):
        return reverse("update-post", kwargs={"slug": self.slug})

    def get_absolute_delete_url(self):
        return reverse('delete', kwargs={"slug": self.slug})


def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(post_pre_save_receiver, sender=Post)
