from django.shortcuts import render
from .models import *
from django.contrib import messages 


# Create your views here.
def home(request):
    products = Product.objects.all() # tek html duhet cikel
    categories = Category.objects.all()
    context = {"products": products, "categories":categories}
    return render(request, "home.html", context)


def about(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request, "category_product.html", context)


def category_products(request, id):
    categories = Category.objects.all()
    categoryDetail = Category.objects.get(pk=id)
    categoryProducts = Product.objects.filter(product_category=categoryDetail)
    context = {"categories" :categories, "categoryDetail":categoryDetail,
              "categoryProducts":categoryProducts}
    return render(request, "category_products.html", context)
   


def contact(request):
    categories = Category.objects.all()
    if request.method == "POST":
        infoFirstName = request.POST["firstName"]
        infoLastName = request.POST["lastName"]
        infoEmail = request.POST["email"]
        infoComment = request.POST["comment"]
        if infoFirstName != "" and infoLastName != "" and InfoEmail !="" and infoComment != "" :
            Contact (
                contact_firstName = infoFirstName,
                contact_lastName = infoLastName,
                contact_email = infoEmail,
                contact_comment = infoComment
            ).save()
            messages.success(request, "Message send!")
        else:
            messages.error(request, "Message not send! Please fill the form.")
    return render(request, "contact.html",context)


def products(request):
    categories = Category.objects.all()
    return render(request, "products.html",context)


def product(request):
    categories = Category.objects.all()
    return render(request, "product.html",context)
