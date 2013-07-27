from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from models import Category

@login_required
def home(request):
    return render(request, "stocks/home.html")

@login_required
def categories(request):
    categories = Category.objects.all()
    return render(request, "stocks/categories/home.html", {
            "categories": categories,
        })
