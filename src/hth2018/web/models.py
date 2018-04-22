from django.db import models

class User(models.Model):
    email = models.EmailField(max_length = 100)
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    password = models.CharField(max_length = 100)
    regdate = models.DateTimeField(auto_now_add = True)
    uni = models.CharField(max_length = 30)

class Listing(models.Model):
    title = models.CharField(max_length = 30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.CharField(max_length = 500)
    postdate = models.DateTimeField(auto_now_add = True)
    # This will be a list/array with the fields UserID, Rating (int), and Review (CharField)
    # Or maybe use foreign keys to assign a separate Ratings class to each Listing instance?
    ratingJSON = models.CharField(max_length = 1000)
