# Generated by Django 5.1.7 on 2025-04-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=240)),
                ('city', models.CharField(max_length=100)),
                ('roll', models.IntegerField(max_length=70)),
            ],
        ),
    ]
