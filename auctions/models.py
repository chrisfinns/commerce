from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils import timezone

class User(AbstractUser):

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_joined = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Auctions(models.Model):
  
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    start_time = models.DateField(auto_now_add=True)
    #bid = models.ForeignKey(Bid, on_delete=models.CASCADE, default=0.00, related_name="bids")
    starting_bid = models.DecimalField(max_digits=14, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")

    class Meta:
        verbose_name_plural = "Auctions" 

    def __str__(self):
        return f"{self.item_name} - {self.description} - {self.watchlist}"


class Bid(models.Model):
    
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE) 
    auction = models.ForeignKey(Auctions, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.amount} on {self.auction}"


class Comments(models.Model):
    auction = models.ForeignKey(Auctions, on_delete=models.CASCADE, related_name="listing")
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user") 
    text = models.TextField() 

    def __str__(self):
        return f"{self.text}"