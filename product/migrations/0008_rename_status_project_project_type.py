# Generated by Django 5.0.1 on 2024-11-16 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_project_recommended_for_you_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='status',
            new_name='Project_Type',
        ),
    ]