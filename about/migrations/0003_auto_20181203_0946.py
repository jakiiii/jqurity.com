# Generated by Django 2.1.3 on 2018-12-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20181203_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='description',
            field=models.TextField(max_length=120),
        ),
    ]