from django.shortcuts import render

from models import Category

def home(request):
    return render(request, "stocks/home.html")

def categories(request):
    categories = Category.objects.all()
    return render(request, "stocks/categories/home.html", {
            "categories": categories,
        })
