# Generated by Django 4.1 on 2022-08-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_dex', '0003_record_owner_alter_record_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='title',
            field=models.CharField(default='New Note', max_length=50),
        ),
    ]
