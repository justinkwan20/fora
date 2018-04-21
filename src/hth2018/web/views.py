from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from web.models import User
from web.models import Listing

# Create your views here.
def index(request):
    user = User.objects.create(username = "wpine215", displayname = "Will", password = "password", email = "wpine@bu.edu")
    listing = Listing.objects.create(title = "Test listing", desc = "This is a test listing.", price = 25, ratingJSON = "5")
    user.save()
    listing.save()
    template = loader.get_template("web/index.html")
    return HttpResponse(template.render({"user_id": user.id, "username": user.username, "title": listing.title, "price": listing.price, "rating": listing.ratingJSON}, request))

# example:
# user.objects.get(id = user.id)
