from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):#(navbar.html line7)href="{{cat.get_url}}":-to create url
        return reverse('shop:products_based_category',args=[self.slug])#(app/urls.py line7)products_based_category was from urls.py on app
                                                    #args was arguments
    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product',blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #we are going to create url that we had already given in app/urls.py product_slug code
    def get_url(self):#if we click on image we need to redirect to that img so this get_url must be passed on category.html
        #so pass this on item/product.image.url line66 on 'a' tag
        return reverse('shop:prodCatdetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name='product'
        verbose_name_plural = 'products'
    def __str__(self):
        return '{}'.format (self.name)
