# Generated by Django 2.2.3 on 2019-10-08 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0003_dishes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dishes',
            old_name='title',
            new_name='name_plat',
        ),
    ]