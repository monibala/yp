# Generated by Django 4.0.5 on 2023-03-13 09:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('who_We_are', ckeditor.fields.RichTextField()),
                ('what_we_do', ckeditor.fields.RichTextField()),
                ('why_choose', ckeditor.fields.RichTextField()),
                ('mission', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
