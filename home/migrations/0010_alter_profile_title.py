# Generated by Django 4.2.5 on 2023-10-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_profile_bio_alter_profile_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.TextField(default=' Ex:- Instagram,Linked-in', max_length=255),
        ),
    ]