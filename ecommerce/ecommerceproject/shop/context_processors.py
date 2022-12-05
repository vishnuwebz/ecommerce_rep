#context processors was used to save all the links in one side
#we are going to set all the links that were neccessory for category.html
from . models import Category

def menu_links(request):#this function is to save the links for menu
    links= Category.objects.all()
    return dict(links=links)#to return as dictionary


'''WE NEED TO MAKE CHANGES IN SETTINGS >TEMPLATES >OPTIONS:{}
'context_processors':[....
'shop.context_processors.menu_links',
]'''
