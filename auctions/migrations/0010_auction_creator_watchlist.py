# Generated by Django 4.2.2 on 2023-07-06 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_auction_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='auctionCreator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observingAuction', to='auctions.auction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
