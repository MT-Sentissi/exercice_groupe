# Generated by Django 2.2.3 on 2019-10-08 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('statut', models.BooleanField(default=True)),
            ],
        ),
    ]