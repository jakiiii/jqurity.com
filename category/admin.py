from django.contrib import admin

from .models.category_models import Category
from .models.subcategory_model import SubCategory


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['category']


class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ['sub_category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
