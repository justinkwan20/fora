from django.contrib import admin
from .models import User
from .models import Listing

class UserAdmin(admin.ModelAdmin):
    fields = ['username','displayname','password','email']

class ListingAdmin(admin.ModelAdmin):
    fields = ['title','desc','price','ratingJSON']

admin.site.register(Listing, ListingAdmin)
admin.site.register(User, UserAdmin)
