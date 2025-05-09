from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homePage"),
    path("about/", views.about, name="aboutPage"),
    path("contact/", views.contact, name="contactPage"),
    path("product/", views.product, name="productPage"),
    path("products/", views.products, name="productsPage"),
    path("category_products/<id>", views.category_products, name="category_productsPage"),
    ]
