from django.contrib import admin
from .models import Auctions
# Register your models here.
class AuctionsAdmin(admin.ModelAdmin):
    list_display =("id", "item_name", "description")



admin.site.register(Auctions, AuctionsAdmin)