# Generated by Django 3.0.5 on 2020-04-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200426_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
    ]