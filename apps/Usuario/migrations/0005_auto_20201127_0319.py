# Generated by Django 3.1.2 on 2020-11-27 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0004_auto_20201127_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='picture',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='perfil/', verbose_name='picture'),
        ),
    ]