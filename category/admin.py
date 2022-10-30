from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name','slug','created','updated')
    readonly_fields = ('created','updated')
    ordering =['-created']


admin.site.register(Category,CategoryAdmin)