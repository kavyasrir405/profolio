# Generated by Django 4.2.5 on 2023-10-07 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Tell us about yourself', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Default_name', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.TextField(default='Ex:- Instagram, Linked-in', max_length=255),
        ),
    ]
