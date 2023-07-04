from django.contrib import admin
from .models import Auctions, User, Comments, Bid
# Register your models here.
class AuctionsAdmin(admin.ModelAdmin):
    list_display =("id", "item_name", "description", )
    filter_horizontal = ('watchlist',)

class MyUserAdmin(admin.ModelAdmin):
    list_display =("id","username", 'email')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("text",)

class BidAdmin(admin.ModelAdmin):
    list_display =("id","amount", "bidder", "auction")

admin.site.register(Auctions, AuctionsAdmin)
admin.site.register(User, MyUserAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Bid,BidAdmin)
