# Generated by Django 3.2.2 on 2021-06-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webera', '0011_auto_20210610_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
