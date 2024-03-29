# Generated by Django 4.1.7 on 2023-04-06 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_userfollows_unique_together_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='userfollows',
            constraint=models.UniqueConstraint(fields=('user', 'followed_user'), name='unique_followers'),
        ),
    ]
