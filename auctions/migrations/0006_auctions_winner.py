# Generated by Django 4.2.2 on 2023-07-09 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctions_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='winner',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
