from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from web.models import User
from web.models import Listing

# Create your views here.
def index(request):
    # This creates temporary database entries
    # user = User.objects.create(username = "wpine215", displayname = "Will", password = "password", email = "wpine@bu.edu")
    # listing = Listing.objects.create(title = "Test listing", desc = "This is a test listing.", price = 25, ratingJSON = "5")
    # user.save()
    # listing.save()

    # This loads the template and returns it to the user
    latest_listings = Listing.objects.order_by('-id')[:10]
    context = {'latest_listings': latest_listings}
    return render(request, 'web/index.html', context)
    #template = loader.get_template("web/index.html")
    #context = {
    #    "user_id": user.id,
    #    "username": user.username,
    #    "title": listing.title,
    #    "price": listing.price,
    #    "rating": listing.ratingJSON
    #    }
    #return HttpResponse(template.render(context, request))

def new_listing(request):
    # database stuff
    template = loader.get_template("web/newlisting.html")
    pass
# example:
# user.objects.get(id = user.id)
