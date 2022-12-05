from django.urls import path
from . import views

app_name = "search_app" #namespacing

urlpatterns = [

    path('',views.SearchResult,name="SearchResult"),

]
