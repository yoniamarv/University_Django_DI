# Generated by Django 2.1.3 on 2018-12-20 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0008_auto_20181220_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='date_naissance',
            new_name='birthdate',
        ),
    ]
