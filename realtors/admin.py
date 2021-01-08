from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email','is_mvp','hire_date')
    list_display_links=('id','name','phone')
    list_editable=('is_mvp',)
    list_filter=('name',)
    list_per_page = 25



admin.site.register(Realtor, RealtorAdmin)
