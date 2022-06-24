from modeltranslation.translator import translator, TranslationOptions
from .models import *

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class MenuTranslationOptions(TranslationOptions):
    fields = ('menu_name',)

class MenuMealTranslationOptions(TranslationOptions):
    fields = ('meal_name',) 
    
translator.register(Category, CategoryTranslationOptions)
translator.register(Menu, MenuTranslationOptions)
translator.register(MenuMeal, MenuMealTranslationOptions)