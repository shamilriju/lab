# Generated by Django 3.2.8 on 2021-12-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
                ('test', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
