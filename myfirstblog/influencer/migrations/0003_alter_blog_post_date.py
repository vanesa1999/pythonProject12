# Generated by Django 3.2 on 2021-04-27 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencer', '0002_auto_20210426_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, help_text='Post Date'),
        ),
    ]