# Generated by Django 4.0.5 on 2023-03-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0004_volunteer_info_ins_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='become_volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('mobile', models.IntegerField(blank=True)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(blank=True)),
            ],
        ),
    ]
