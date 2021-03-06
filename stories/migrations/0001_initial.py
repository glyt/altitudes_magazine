# Generated by Django 3.0.8 on 2020-07-08 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
