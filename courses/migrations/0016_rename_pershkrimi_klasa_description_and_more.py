# Generated by Django 4.1.3 on 2022-12-13 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_alter_klasa_imazhi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klasa',
            old_name='pershkrimi',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='klasa',
            old_name='imazhi',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='klasa',
            old_name='titulli',
            new_name='title',
        ),
    ]
