# Generated by Django 2.2.7 on 2019-11-07 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191107_0311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='categories',
            new_name='category',
        ),
    ]
