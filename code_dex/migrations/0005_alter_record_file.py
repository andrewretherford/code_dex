# Generated by Django 4.1 on 2022-08-25 22:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_dex', '0004_record_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='file',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'ppt', 'xlsx', 'png', 'jpg'])]),
        ),
    ]