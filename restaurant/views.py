from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from .models import Category, Gallery, Menu
# Create your views here.

def home(request):
    context = {
        "last_added_menus":Menu.objects.order_by('-date_added')[:4],
    }
    return render(request,'restaurant/index.html', context)

def translate(language):
    cur_language = get_language()
    try: 
        activate(language)
    except:
        activate(cur_language)

def address_map(request):
    return render(request,'restaurant/address.html')
    
def contact(request):
    return render(request,'restaurant/contact.html')

def gallery(request):
    context = {
        'gallery_images':Gallery.objects.all(),
    }
    return render(request,'restaurant/gallery.html', context)

def menu(request, category_id):
    ctg = get_object_or_404(Category, pk = category_id)
    ctg_menu = ctg.menu.all()
    
    context = {
        'categories':Category.objects.all(),
        'menus':ctg_menu,
    }
    return render(request,'restaurant/menu.html', context)