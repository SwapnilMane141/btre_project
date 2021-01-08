from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','listing','listing_id','name','email','message')
    list_display_links = ('id','listing','name')
    search_fields = ('name','email','listing')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
