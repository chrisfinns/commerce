from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta



class User(AbstractUser):
    # auction listings, bids, comments, and auction categories. 
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_joined = models.DateField(auto_now_add=True)

    

class Bids(models.Model):
    
    # bid_amount, connect to the user/auction
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True)
    #bidder =
    #timestamp = 

class Auctions(models.Model):
    def now_plus_7(): 
        return datetime.now() + timedelta(days = 7)

    # auction_items, who was the user that bid on it, bid_amount
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='auction_images')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(default=now_plus_7)
    starting_price = models.DecimalField(max_digits=14, decimal_places=2)
    bids = models.ForeignKey(Bids, on_delete=models.CASCADE, related_name=)
    #seller =
    #is_active =
  

    def __str__(self):
        return f"{self.id}: {self.item_name} - {self.description}"





class Comments():
    #what auction is it linked to, user_comment, 
    #auction
    #commenter
    #text
    #timestamp

    pass