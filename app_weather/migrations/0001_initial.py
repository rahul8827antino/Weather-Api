# Generated by Django 4.1.5 on 2023-01-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=100)),
                ('temp_min', models.FloatField()),
                ('temp_max', models.FloatField()),
                ('pressure', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('sunrise_time', models.DateTimeField()),
                ('sunset_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]