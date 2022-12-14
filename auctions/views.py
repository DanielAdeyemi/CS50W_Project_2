from unicodedata import category
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import auctions

from .models import Listing, User, Comment, Bid


def index(request):
    return render(request, "auctions/index.html", {
        'listings': Listing.objects.all()
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


def listing(request, listing_id=None):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, auctions/listing.html, {
        "listing": listing
    })


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        current_bid = request.POST['starting_bid']
        picture = request.POST['img_url']
        category = request.POST['category']
        bid = Bid.objects.create(initial_bid=current_bid)
        comments = Comment.objects.create(comment="")
        creator = User.objects.get(pk=1)
        listing = Listing.objects.create(
            title=title, description=description, current_bid=bid, picture=picture, category=category, comments=comments, creator=creator)
        listing.save()
        return HttpResponseRedirect(reverse('index'))
        pass
    else:
        return render(request, "auctions/create.html")
