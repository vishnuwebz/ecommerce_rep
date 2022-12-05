from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.

#to view allproducts while we click ALLPRODUCTS link in navbar

def allProdCat(request,c_slug=None):
    c_page=None
    products_list=None
    products = None
    if c_slug != None:#if not none
        c_page=get_object_or_404(Category,slug=c_slug)
        #if there is nothing in c_page it will show 404 error otherwise it will do filter
        #we need to display the products inside the category page
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)
        #whatever products are available as true it will display
    #paginator code:
    paginator = Paginator(products_list,6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
    #it can come error so we're going to write try code
    return render(request,"category.html",{'category':c_page,'products':products})

def proDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})

