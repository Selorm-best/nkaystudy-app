# Generated by Django 4.1.3 on 2022-12-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20200317_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klasa',
            name='imazhi',
            field=models.ImageField(default='cat_images/default.jpg', upload_to='cat_images'),
        ),
    ]
