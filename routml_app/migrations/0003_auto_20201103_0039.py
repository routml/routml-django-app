# Generated by Django 3.1.2 on 2020-11-02 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routml_app', '0002_url_day_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='day_created',
            new_name='date',
        ),
    ]