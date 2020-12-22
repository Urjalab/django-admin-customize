# Generated by Django 3.1.4 on 2020-12-22 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('salary', models.FloatField()),
                ('is_married', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('-salary', 'name'),
            },
        ),
    ]
