# Generated by Django 3.1.1 on 2020-10-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='app_name',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
