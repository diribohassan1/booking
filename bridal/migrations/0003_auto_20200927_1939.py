# Generated by Django 3.1 on 2020-09-27 16:39

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridal', '0002_auto_20200917_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page_inf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=15)),
                ('keywords', models.CharField(blank=True, max_length=15)),
                ('description', models.CharField(blank=True, max_length=20)),
                ('company', models.CharField(blank=True, max_length=15)),
                ('address', models.CharField(blank=True, max_length=15)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=15)),
                ('facebook', models.CharField(blank=True, max_length=20)),
                ('instagram', models.CharField(blank=True, max_length=20)),
                ('twitter', models.CharField(blank=True, max_length=20)),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='gowns',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]