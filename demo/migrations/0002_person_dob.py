# Generated by Django 3.1.4 on 2020-12-22 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
