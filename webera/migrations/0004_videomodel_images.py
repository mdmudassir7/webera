# Generated by Django 3.2.2 on 2021-06-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webera', '0003_coursemodel_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='videomodel',
            name='images',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]