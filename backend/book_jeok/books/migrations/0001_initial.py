# Generated by Django 4.1 on 2023-02-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('pubdate', models.DateTimeField()),
                ('path', models.CharField(max_length=255)),
            ],
        ),
    ]
