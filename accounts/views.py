from django.shortcuts import render,redirect
from .forms import Signupuser,Editprofile,Resetpass,Loginform
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
def login_user(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('root:home')
            else:
                messages.add_message(request,messages.ERROR,'not valid')
                return redirect('accounts:login')
        else:
            messages.add_message(request,messages.ERROR,'not valid')
            return redirect('accounts:login')
    else:
        return render(request,'registrations/login.html')


        
            

def logout_user(request):
    logout(request)
    return redirect('root:home')

def signup_user(request):
    if request.method == 'POST':
        form = Signupuser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('root:home')
        else:
            messages.add_message(request,messages.ERROR,'not valid')
            return render(request,'registrations/signup.html')
    else:
        return render(request,'registrations/signup.html')


def change_password(request):
    pass

def reset_password(request):
    pass

def reset_password_done(request):
    pass

def reset_password_confirm(request, token):
    pass

def reset_password_complete(request):
    pass

def edit_profile(request, id):
    user_profile = Profile.objects.get(user=id)
    if request.method == 'POST':
        form = Editprofile(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'ok')
            return redirect('accounts:edit_profile')
        else:
            messages.add_message(request,messages.ERROR,'not valid')
            return redirect('accounts:edit_profile')
    else:
        return render(request,'registrations/edit-profile.html')
