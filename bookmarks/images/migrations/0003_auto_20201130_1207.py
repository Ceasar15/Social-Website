# Generated by Django 3.1.3 on 2020-11-30 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20201128_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='images',
            new_name='image',
        ),
    ]