from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    pass


class Auctions(models.Model):
    # auction_items, who was the user that bid on it, bid_amount
    item_name = models.CharField(max_length=64)
    description = models.CharField(max_length=528)
    #photo = URL
    #bid = ForeignKey
    #created

    def __str__(self):
        return f"{self.id}: {self.item_name} - {self.description}"


class Bids():
    # bid_amount, connect to the user/auction
    pass


class Comments():
    #what auction is it linked to, user_comment, 
    pass