# Generated by Django 3.2.2 on 2021-06-09 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webera', '0009_alter_videomodel_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='images',
            field=models.ImageField(default='images/video_hjR01iq.png', upload_to='images/'),
        ),
    ]