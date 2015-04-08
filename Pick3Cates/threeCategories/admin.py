from django.contrib import admin
from threeCategories.models import category


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name')
    list_filter = ['name']
admin.site.register(category)

# Register your models here.
