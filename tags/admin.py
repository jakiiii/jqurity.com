from django.contrib import admin
from .models import Tag


# Register your models here.
class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag']


admin.site.register(Tag, TagAdmin)
