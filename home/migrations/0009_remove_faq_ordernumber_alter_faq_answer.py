# Generated by Django 5.0.1 on 2024-11-13 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_setting_some_faq_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='ordernumber',
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(max_length=1000),
        ),
    ]