from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    #username
    #email
    #password
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_joined = models.DateField(auto_now_add=True)
    

class Bids(models.Model):
    
    # bid_amount, connect to the user/auction
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True)
    #auction = 

    #bidder =
    #timestamp = 

class Auctions(models.Model):
    # auction_items, who was the user that bid on it, bid_amount
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='auction_images')
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateTimeField(default=datetime.now + timedelta(days=7))
    starting_price = models.DecimalField(max_digits=14, decimal_places=2)
    #current_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True)
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