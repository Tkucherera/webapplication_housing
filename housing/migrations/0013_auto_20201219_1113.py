# Generated by Django 3.1.3 on 2020-12-19 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0012_auto_20201217_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='username',
            new_name='user',
        ),
    ]
