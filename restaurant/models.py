from email.policy import default
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    
    
class Menu(models.Model):
    menu_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name="menu", on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(default='images/default.png',upload_to='images')
    
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.menu_name
    
class MenuMeal(models.Model):
    meal_name = models.CharField(max_length=50)
    price = models.FloatField(blank=False)
    menu = models.ForeignKey(Menu, related_name="menu_meals", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.menu} - {self.meal_name}'

class Gallery(models.Model):
    image = models.ImageField(default='images/default.png', upload_to='images', null=True)
    
    class Meta:
        verbose_name_plural = "Galleries"
        
    def __str__(self):
        return f'Image {self.id}'