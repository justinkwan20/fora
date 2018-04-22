from django import forms
from .models import User
from .models import Listing

class RegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'password', 'uni')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

class NewListForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'price', 'desc')
