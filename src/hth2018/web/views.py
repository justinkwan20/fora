from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from web.models import Listing
from .forms import RegForm
from .forms import LoginForm
from .forms import NewListForm
from django.shortcuts import redirect
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your views here.

def home(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        username = "testuser" #request.POST.get('username')
        password = request.POST.get('password')
        # Create user and save to the database
        user = User.objects.create_user(username = username, email = email, password = password)
        # Update fields and then save again
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        return redirect('/accounts/login')
    elif request.method == 'GET':
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
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        ratingJSON = 10
        newlisting = Listing.objects.create(title = title, price = price, desc = desc, ratingJSON = ratingJSON)
        newlisting.save()
        return redirect('/listings')
    elif request.method == 'GET':
        return render(request, 'web/base_newlisting.html')

def register(request):
    return render(request, 'web/base_register.html')

def login(request):
    return render(request, 'web/base_login.html')

# example:
# user.objects.get(id = user.id)
