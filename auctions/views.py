from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import decimal


from .models import User, Auctions, Comments, Bid


def index(request):
    auctions = Auctions.objects.all()

    return render(request, "auctions/index.html", {
        "auctions": auctions
    })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def createListing(request):

        
    return render(request, "auctions/createlisting.html")
    

def active(request):
    auctions = Auctions.objects.all()

    return render(request, "auctions/index.html", {
        "auctions": auctions
    })


def listings(request, listing_id):
    listing = Auctions.objects.get(pk=listing_id)
    comments = Comments.objects.filter(auction=listing_id)
    bids = Bid.objects.filter(auction=listing_id)
    #starting_price = Auctions.objects.get()
    #highest_bid = Bid.objectsget

    startingPrice = int(listing.starting_bid)
    currentPrice = startingPrice

    for bid in bids:
        if bid.amount > decimal.Decimal(currentPrice):
            currentPrice = bid.amount
        print(currentPrice)



    return render(request, "auctions/listings.html", {
        "listing": listing, 
        "comments": comments,
        "currentPrice": currentPrice,
                    #all the arugments in the HTML will come from this dict item
    })



def watch(request):

    return render(request, "auctions/watchlist.html")