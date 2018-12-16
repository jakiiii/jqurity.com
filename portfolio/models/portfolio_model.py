import os
import random
from django.db import models


def get_filename_exist(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(inistance, file_name):
    new_filename = random.randint(1, 101119)
    name, ext = get_filename_exist(file_name)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "slider/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


# Create your models here.
class PortfolioModel(models.Model):
    project_name = models.CharField(max_length=40)
    image = models.ImageField(upload_to=upload_image_path)
    git_link = models.URLField(max_length=300, null=True, blank=True)
    web_link = models.URLField(max_length=300, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
