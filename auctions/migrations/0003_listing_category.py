# Generated by Django 4.1 on 2022-09-07 03:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]