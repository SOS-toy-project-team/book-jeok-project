# Generated by Django 4.1 on 2023-03-27 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='reviews.review'),
        ),
    ]
