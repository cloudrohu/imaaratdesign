# Generated by Django 5.0.1 on 2024-11-13 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_slider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_page',
            name='experience',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='about_page',
            name='technician',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]