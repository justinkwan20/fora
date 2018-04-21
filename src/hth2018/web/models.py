from django.db import models

# Create your models here.
# User class should not be used yet
class User(models.Model):
    # No user ID field necessary, Django automatically creates an ID row in database
    username = models.CharField(max_length = 20)
    displayname = models.CharField(max_length = 30)
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    # regdate = models.DateTimeField()

    # university = models.CharField(max_length = 30)
    # location = models.CharField(max_length = 30)
    # Need to implement profile pics

class Listing(models.Model):
    # No listing ID field necessary, Django automatically creates an ID row in database
    title = models.CharField(max_length = 30)
    desc = models.CharField(max_length = 500)
    price = models.IntegerField()
    # Need to implement photo preview/gallery (optional field)

    # This will be a list/array with the fields UserID, Rating (int), and Review (CharField)
    ratingJSON = models.CharField(max_length = 1000)
