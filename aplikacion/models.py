from django.db import models


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True)
    category_image = models.ImageField(upload_to="category/", null=True, blank=True)
    category_description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.category_name}"

class Product(models.Model):
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_image = models.ImageField(upload_to="product/", null=True, blank=True)
    product_image1 = models.ImageField(upload_to="product/", null=True, blank=True)
    product_description = models.TextField(max_length=1000, null=True, blank=True)
    product_price = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, blank=True
    )
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.product_name}"
class Contact (models.Model):
        contact_firstName = models.CharField(max_length=100,null=True,blank=True)
        contact_lastName = models.CharField(max_length=100,null=True,blank=True)
        contact_email = models.EmailField(null=True,blank=True)
        conatct_comment = models.TextField(max_length=1000,null=True,blank=True)

        def __str__(self):
            return f"{self.contact_firstName} {self.contact_lastName}"
  

 
