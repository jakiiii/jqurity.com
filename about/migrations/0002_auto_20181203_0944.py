# Generated by Django 2.1.3 on 2018-12-03 09:44

import about.models.about_model
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=about.models.about_model.upload_image_path),
        ),
    ]
