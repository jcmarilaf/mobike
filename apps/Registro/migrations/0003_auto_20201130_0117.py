# Generated by Django 3.1.2 on 2020-11-30 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='post/', verbose_name='picture'),
        ),
    ]