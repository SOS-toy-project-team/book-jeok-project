# Generated by Django 4.1.7 on 2023-02-15 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('file_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
    ]
