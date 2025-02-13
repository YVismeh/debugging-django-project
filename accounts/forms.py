from django import forms
from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm


class Signupuser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email','password1','password2']
        

class Editprofile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username','image','id_code','phone']

class Loginform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

class Resetpass(forms.Form):
    email = forms.EmailField()

