# Generated by Django 4.0.1 on 2022-04-23 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Project_link',
            new_name='project_link',
        ),
    ]
