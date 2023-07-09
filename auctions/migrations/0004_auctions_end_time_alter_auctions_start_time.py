# Generated by Django 4.2.2 on 2023-07-09 02:29

import auctions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auctions_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='end_time',
            field=models.DateTimeField(default=auctions.models.Auctions.auctionlength),
        ),
        migrations.AlterField(
            model_name='auctions',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]