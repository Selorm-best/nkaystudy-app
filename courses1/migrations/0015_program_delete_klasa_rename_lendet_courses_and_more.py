# Generated by Django 4.1.3 on 2022-12-09 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0014_auto_20200317_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulli', models.CharField(max_length=150)),
                ('pershkrimi', models.TextField(max_length=200, null=True)),
                ('imazhi', models.ImageField(default='cat_images/default.jpg', upload_to='cat_images')),
            ],
        ),
        migrations.DeleteModel(
            name='Klasa',
        ),
        migrations.RenameModel(
            old_name='Lendet',
            new_name='Courses',
        ),
        migrations.AlterField(
            model_name='courses',
            name='klasa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.program'),
        ),
    ]