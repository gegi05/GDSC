# Generated by Django 5.1.dev20231212045133 on 2023-12-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_yourmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourmodel',
            name='field1',
            field=models.CharField(default='take your dream and hold it as it is your life', max_length=200),
        ),
        migrations.AlterField(
            model_name='yourmodel',
            name='field2',
            field=models.FileField(default='tests.py', upload_to='static/'),
        ),
    ]