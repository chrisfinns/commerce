from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import decimal
from .forms import NewListing, Watchlist
from django.contrib.auth.decorators import login_required
from django.db.models import Subquery, OuterRef, Max
from django.contrib import messages



from .models import User, Auctions, Comments, Bid, Category

    
    

def index(request):
    
    auctions = Auctions.objects.filter(is_active=True)

        
    for auction in auctions:
        current_bid = Bid.objects.filter(auction=auction).order_by('-amount').first()
        auction.current_bid = current_bid.amount if current_bid else auction.starting_bid

        Auctions.update_status(auction)


 

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
    



def listings(request, listing_id):
    listing = Auctions.objects.get(pk=listing_id)
    comments = Comments.objects.filter(auction=listing_id)
    startingPrice = int(listing.starting_bid)
    bids = Bid.objects.filter(auction=listing_id)
    count = Bid.objects.filter(auction=listing_id).count()
    
    Auctions.update_status(listing)


### BIDDING SYSTEM ###
    currentPrice = startingPrice
    for bid in bids:
        if bid.amount > decimal.Decimal(currentPrice):
            currentPrice = bid.amount



### WATCHLIST ###
    status = request.POST.get("watchlist")
    user = request.user

    if status == "True":
        
        user.watchlist.remove(listing)
   
    if status == "False":
            user.watchlist.add(listing)

    
    ### END LISTING ###

    return render(request, "auctions/listings.html", {
        "listing": listing, 
        "comments": comments,
        "currentPrice": currentPrice,
        "bidcount": count,
        "user": user
                    #all the arugments in the HTML will come from this dict item
    })

@login_required
def createlisting(request):
    if request.method == "POST":
        form = NewListing(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            categories = form.cleaned_data['categories']

            category_instance = categories.first()


            descriptionForm = form.cleaned_data.get("description")
            urlForm = form.cleaned_data.get("url")
            starting_priceForm = form.cleaned_data.get("starting_price")
            user_id = request.user
            auction = Auctions(item_name=title, description=descriptionForm, image=urlForm, starting_bid = starting_priceForm, seller=user_id, category=category_instance )
            auction.save()


    else:
        form = NewListing()
    

    return render(request, "auctions/createlisting.html", {
        "form": form,
    })

@login_required
def watch(request):
    user = request.user
    watchlist_auctions = user.watchlist.all()
           
    return render(request, "auctions/watchlist.html", {
        "watchlist_auctions": watchlist_auctions
    })



@login_required
def bid(request, listing_id):
    listing = Auctions.objects.get(pk=listing_id)
    current_bid = Bid.objects.filter(auction=listing).order_by('-amount').first()
#     bids = Bid.objects.filter(auction=listing_id)
#     startingPrice = int(listing.starting_bid)
# ### BIDDING SYSTEM ###
#     currentPrice = startingPrice
#     for bid in bids:
#         if bid.amount > decimal.Decimal(currentPrice):
#             currentPrice = bid.amount
    user = request.user

    

    if request.method == "POST" and user != listing.seller:
        Auctions.update_status(listing)

        user = request.user
        bidamount = decimal.Decimal(request.POST.get("bid"))

        if current_bid is None:
            if bidamount >= listing.starting_bid:

                bid = Bid(amount=bidamount, bidder=user, auction=listing)
                bid.save()

            else:
                messages.warning(request, 'Invalid Bid')
        
        elif bidamount > current_bid.amount:

            bid = Bid(amount=bidamount, bidder=user, auction=listing)
            bid.save()
        
        else:
            messages.warning(request, 'Invalid Bid') 

        return HttpResponseRedirect(reverse("listing", args=[listing.id]))
    
    else:
        messages.warning(request, 'You are the Seller') 
        return HttpResponseRedirect(reverse("listing", args=[listing.id]))




def end_auction(request, listing_id):
    listing = Auctions.objects.get(pk=listing_id)
    current_bid = Bid.objects.filter(auction=listing).order_by('-amount').first()

    if current_bid:
        listing.winner = current_bid.bidder
        listing.is_active = False
        listing.save()
        


    return HttpResponseRedirect(reverse("listing", args=[listing.id]))


def add_comment(request, listing_id):
    
    listing = Auctions.objects.get(pk=listing_id)
    #bidamount = decimal.Decimal(request.POST.get("bid"))
    comment_text = request.POST.get("comment-field")

    comment = Comments(auction=listing, commenter=request.user, text=comment_text)
    comment.save()

    

    return HttpResponseRedirect(reverse("listing", args=[listing_id]))


def categories(request):
    categories = Category.objects.all()
    print(categories)
    

    return render(request, "auctions/categories.html", {
        "categories": categories
    })
    

def category_listings(request, category):
    auctions = Auctions.objects.filter(category__name=category)
    
    return render(request, 'auctions/category_listings.html', {
        'auctions': auctions, 
        'category': category
        })