from django.urls import path
from .models import Auctions

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories/", views.categories, name="categories"),
    path("categories/<str:category>/", views.category_listings, name="category_listings"),

    path("createlisting", views.createlisting, name="createlisting"),
    path("listings/<int:listing_id>", views.listings, name="listing"),
    path("watchlist", views.watch, name="watch"),
    path("bid/<int:listing_id>/", views.bid, name="bid"),
    path("end_auction/<int:listing_id>/", views.end_auction, name='end_auction'),
    path("comment/<int:listing_id>/", views.add_comment, name='add_comment')

    ]
