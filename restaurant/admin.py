from django.contrib import admin
from . import models
from modeltranslation.admin import TranslationAdmin

class CategoryAdmin(TranslationAdmin):
    pass

class MenuAdmin(TranslationAdmin):
    pass

class MenuMealAdmin(TranslationAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.MenuMeal, MenuMealAdmin)
admin.site.register(models.Gallery)
