from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from web.models import User
from web.models import Listing

# Create your views here.

def home(request):
    return render(request, 'web/base_home.html')

def index(request):
    # This creates temporary database entries
    # user = User.objects.create(username = "wpine215", displayname = "Will", password = "password", email = "wpine@bu.edu")
    # listing = Listing.objects.create(title = "Test listing", desc = "This is a test listing.", price = 25, ratingJSON = "5")
    # user.save()
    # listing.save()

    # This loads the template and returns it to the user
    latest_listings = Listing.objects.order_by('-id')[:10]
    context = {'latest_listings': latest_listings}
    return render(request, 'web/base_listings.html', context)
    #template = loader.get_template("web/index.html")
    #context = {
    #    "user_id": user.id,
    #    "username": user.username,
    #    "title": listing.title,
    #    "price": listing.price,
    #    "rating": listing.ratingJSON
    #    }
    #return HttpResponse(template.render(context, request))

def new(request):
    # database stuff
    return render(request, 'web/base_newlisting.html')

def register(request):
    # database stuff
    return render(request, 'web/base_register.html')

def login(request):
    # database stuff
    return render(request, 'web/base_login.html')

# example:
# user.objects.get(id = user.id)
