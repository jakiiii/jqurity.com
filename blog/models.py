import os
import random
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='media')


def get_filename_exist(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(inistance, file_name):
    new_filename = random.randint(1, 101119)
    name, ext = get_filename_exist(file_name)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "banner/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


# Create your models here.
class Blog(models.Model):
    heading = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    banner = models.ImageField()

    def __str__(self):
        return "Banner Image"
