# Generated by Django 2.1.3 on 2018-12-06 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='coefficiant',
            new_name='coefficient',
        ),
    ]
