# Generated by Django 2.1.3 on 2018-12-20 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0007_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='nom',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='prenom',
            new_name='last_name',
        ),
    ]