# Generated by Django 3.0.5 on 2020-04-22 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200421_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques',
            field=models.CharField(max_length=100000),
        ),
    ]