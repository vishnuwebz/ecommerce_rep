from .import views
from django.urls import path
app_name='shop'#namespacing
urlpatterns=[
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_based_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
]