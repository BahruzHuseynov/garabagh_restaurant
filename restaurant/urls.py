from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
    path('menu/<int:category_id>', views.menu, name="menu"),
    path('map/', views.address_map, name="address"),
]
