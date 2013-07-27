from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    return render(request, "users/login.html")

def user_authenticate(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect("/stocks/")
        else:
            messages.error(request, "Account has been disactivated.")
            return redirect("/users/login/")
    else:
        messages.error(request, "Invalid username or password")
        return redirect("/users/login/")
