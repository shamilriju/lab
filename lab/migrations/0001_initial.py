# Generated by Django 3.2.8 on 2021-12-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
                ('procedures', models.CharField(max_length=200)),
            ],
        ),
    ]