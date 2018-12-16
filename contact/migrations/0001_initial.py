# Generated by Django 2.1.3 on 2018-12-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=32)),
                ('subject', models.CharField(max_length=120)),
                ('context', models.TextField(max_length=500)),
                ('default_email', models.EmailField(blank=True, max_length=32, null=True)),
            ],
        ),
    ]
