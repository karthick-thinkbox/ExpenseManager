from django.contrib import admin
from .models import expense,category
class expense_admin(admin.ModelAdmin):
    search_fields=('category','user','date',)
    list_display=('date','user','category','amount','Description',)
    list_filter=('date','user','category',)
    
class cat_admin(admin.ModelAdmin):
    search_fields=('value',)
    
admin.site.register(expense,expense_admin)
admin.site.register(category,cat_admin)

admin.site.site_header = 'FulfilIo Admin'