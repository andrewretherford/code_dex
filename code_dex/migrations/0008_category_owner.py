# Generated by Django 4.1 on 2022-08-28 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('code_dex', '0007_alter_record_category_alter_record_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
