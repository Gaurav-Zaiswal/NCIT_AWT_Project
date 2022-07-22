from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
# from .models import User


# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, "socialapp/home.html", {}) 


def profile(request, name):
    return render(request, "socialapp/index.html", {'name':"Gaurav Js"})    


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f"Welcome {username} to Advanced CRM console!")
            return redirect("socialapp:home")
    form = UserCreationForm()
    return render(request, 'socialapp/register.html', {'form': form})


def admin(request):
    return render(request, "admin.html", {}) 
